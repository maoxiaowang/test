# coding=utf-8
"""
Exceptions codes:
10000 - 10999: identity
"""
from common.exceptions import ECloudException
from django.utils.translation import ugettext_lazy as _


class InvalidPassword(ECloudException):
    code = 10000
    desc = 'Invalid password'


class NoSuchUsername(ECloudException):
    code = 10001
    desc = 'No such username'


class InvalidUsernameFormat(ECloudException):
    code = 10002
    desc = 'Invalid username format'


class InvalidPasswordFormat(ECloudException):
    code = 10003
    desc = 'Invalid password format'


class InvalidEmailFormat(ECloudException):
    code = 10004
    desc = 'Invalid email format'


class InvalidGroupFormat(ECloudException):
    code = 10005
    desc = 'Invalid group format'


# group: 10100 - 10199

class GroupDeletingError(ECloudException):
    code = 10100
    desc = 'Group deleting error'


# user: 10200 - 10299
class UserDeletingError(ECloudException):
    code = 10200
    desc = 'User deleting error'
