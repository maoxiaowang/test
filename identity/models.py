# coding=utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _
# from common.utils.validators import validate_password, validate_email
from django.contrib.auth.models import AbstractUser, UserManager, AnonymousUser, Permission, Group
from django.contrib.auth.validators import (
    ASCIIUsernameValidator, UnicodeUsernameValidator)
from uuid import uuid4


# Create your models here.


class MyUserManager(UserManager):
    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        # extra_fields could contain more fields
        return self._create_user(username, email, password, **extra_fields)


class UserModel(AbstractUser, MyUserManager):
    """
    用户
    """
    username_validator = ASCIIUsernameValidator()

    id = models.CharField(_('id'), max_length=36,
                          primary_key=True, default=uuid4(), unique=True)

    class Meta:
        ordering = ["-username"]

    def __str__(self):
        return self.username


class GroupModel(Group):
    """
    用户组
    """
    pass


class PermissionModel(Permission):
    """
    权限
    Three basic permissions -- add, change and delete -- are automatically
    created for each Django model.
    """
    pass


class AnonymousUserModel(AnonymousUser):
    """
    匿名用户
    """
    pass
