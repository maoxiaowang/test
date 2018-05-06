# coding=utf-8
from common.utils.string_ import UUID

from django.contrib.auth import get_user_model
from django.contrib.auth.models import (AbstractUser, BaseUserManager,
                                        Group, Permission)
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


# Create your models here.


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not username:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        self.model = get_user_model()
        username = self.model.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('id', UUID.uuid4)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, email, password, **extra_fields)


class User(AbstractUser, UserManager):
    """
    用户
    """
    username_validator = ASCIIUsernameValidator()
    id = models.CharField(
        _('id'),
        max_length=36,
        primary_key=True,
        unique=True)
    groups = models.ManyToManyField(
        Group)
    user_permissions = models.ManyToManyField(
        Permission)

    username = models.CharField(
        _('username'),
        max_length=32,
        unique=True,
        help_text=_(
            'Required. 150 characters or fewer. '
            'Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    email = models.EmailField(_('email address'), blank=True)

    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        db_table = 'auth_user'
        ordering = ['username']
        verbose_name = _('user')
        verbose_name_plural = _('users')
        permissions = (
            ('list_user', _('Can see user list')),
            ('detail_user', _('Can see user detail')),
            ('create_user', _('Can create user')),
            ('update_user', _('Can update user')),
            ('delete_user', _('Can delete user')),
            ('update_user_permission', _('Can change user permission')),
        )
        default_permissions = ()

    def __str__(self):
        return self.username

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)


class Tenant(models.Model):
    """
    需要和keystone的tenant保持一致
    """

    id = models.CharField(max_length=36, verbose_name='id', primary_key=True)
    name = models.CharField(max_length=64)
    user = models.ManyToManyField(User)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'auth_tenant'
