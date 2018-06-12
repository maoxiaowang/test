# coding=utf-8
from common.utils.text_ import UUID, obj2iter

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


class ResourceMixin:
    """
    User resource management
    """

    def has_resource(self, resource_id):
        return Resource.objects.filter(id=resource_id, user=self).exists()

    def get_resources(self, resource_type=None):
        if resource_type:
            return Resource.objects.filter(user=self, type=resource_type)
        return Resource.objects.filter(user=self)

    def assign_resource(self, resource_id, resource_type):
        obj = Resource.objects.filter(id=resource_id)
        if obj.exists():
            obj.update(user=self)
        else:
            Resource.objects.create(id=resource_id,
                                    type=resource_type,
                                    user=self)

    def delete_resource(self, resource_id):
        Resource.objects.get(pk=resource_id, user=self).delete()

    def undo_assign_resource(self, resource_ids=None):
        """
        Remove resource(s) assignment from a user
        :param resource_ids: [list|tuple|None]
        :return:
        """
        if resource_ids:
            assert isinstance(resource_ids, (list, tuple, str))
            Resource.objects.filter(id__in=obj2iter(resource_ids)).update(user_id=None)
        else:
            Resource.objects.filter(user=self).update(user_id=None)


class User(ResourceMixin, AbstractUser, UserManager):
    """
    Custom user model
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
            ('add_user', _('Can add user')),
            ('change_user', _('Can change user')),
            ('delete_user', _('Can delete user')),
            ('change_user_permission', _('Can change user permission')),
            ('change_user_group', _('Can change user group'))
        )
        default_permissions = ()

    def __str__(self):
        return self.username

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def delete(self, using=None, keep_parents=False):
        # need to remove user's resources first
        self.undo_assign_resource()
        super().delete(using=using, keep_parents=keep_parents)


class Project(models.Model):
    """
    需要和keystone的tenant/project保持一致
    """

    id = models.CharField(max_length=36, verbose_name='id', primary_key=True)
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'auth_tenant'


class Resource(models.Model):
    """
    User's resource assignment
    """
    id = models.CharField(primary_key=True, max_length=36)
    type = models.CharField(max_length=255, verbose_name=_('type'))
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['type', 'id']
        db_table = 'resource'
        permissions = (
            # ('list_storage', _('Can see storage list')),
            # ('detail_storage', _('Can see storage detail')),
            # ('add_storage', _('Can add storage')),
            # ('change_storage', _('Can change storage')),
            # ('delete_storage', _('Can delete storage')),

            # ('list_volume', _('Can see volume list')),
            # ('detail_volume', _('Can see volume detail')),
            # ('add_volume', _('Can add volume')),
            # ('change_volume', _('Can change volume')),
            # ('delete_volume', _('Can delete volume')),

            # ('list_host', _('Can see host list')),
            # ('detail_host', _('Can see host detail')),
            # ('add_host', _('Can add host')),
            # ('change_host', _('Can change host')),
            # ('delete_host', _('Can delete host')),
        )
        default_permissions = ()
        app_label = 'resource'

