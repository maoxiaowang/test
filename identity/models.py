# coding=utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _
from common.utils.validators import validate_password, validate_email
from django.contrib.auth.models import User, AnonymousUser, Permission, Group
from django.contrib.auth.validators import ASCIIUsernameValidator

# Create your models here.


class UserModel(User):
    """
    用户
    """
    username_validator = ASCIIUsernameValidator()

    password = models.CharField(max_length=32, verbose_name=_('password'))
    username = models.CharField(max_length=16, verbose_name=_('username'),
                                validators=[username_validator])
    email = models.EmailField(max_length=64, verbose_name=_('email'),
                              validators=[validate_email])

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
    """
    pass


class AnonymousUserModel(AnonymousUser):
    """
    匿名用户
    """
    pass