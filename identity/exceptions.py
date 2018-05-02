# coding=utf-8
"""
Exceptions codes:
10000 - 10999: identity
"""
from common.exceptions import ECloudException
from django.utils.translation import ugettext_lazy as _


class InvalidPassword(ECloudException):
    code = 10000
    desc = _('Invalid password')


class NoSuchUsername(ECloudException):
    code = 10001
    desc = _('No such username')


class InvalidUsernameFormat(ECloudException):
    code = 10002
    desc = _('Invalid username format')


class InvalidPasswordFormat(ECloudException):
    code = 10003
    desc = _('Invalid password format')


class InvalidEmailFormat(ECloudException):
    code = 10004
    desc = _('Invalid email format')


class InvalidGroupFormat(ECloudException):
    code = 10005
    desc = _('Invalid group format')
