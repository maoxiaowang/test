# coding=utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _
# from common.utils.validators import validate_password, validate_email
from django.contrib.auth.models import User, AnonymousUser, Permission, Group
from django.contrib.auth.validators import (
    ASCIIUsernameValidator, UnicodeUsernameValidator)
from uuid import uuid4


# Create your models here.


class UserModel(User):
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

    @property
    def full_name(self):
        "Returns the person's full name."
        return '%s %s' % (self.first_name, self.last_name)




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
