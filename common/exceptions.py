# coding=utf-8
"""
Exceptions codes:
1 - 599: Http
600 - 999: common

1000 - 1999: OpenStack

Exceptions level:
error, warning, info

Exceptions desc:
short and accurate description for an exception
"""
from django.utils.translation import gettext_lazy as _
from django.utils.text import format_lazy


class ECloudException(Exception):
    # Base view exception
    # level: error, warning, info
    level = 'error'
    desc = 'Undefined exception'
    code = 0

    def __init__(self, msg=None):
        if msg and isinstance(msg, str):
            msg = _(msg)
        self.msg = msg

    def __str__(self):
        if self.msg:
            return format_lazy('{desc}: {msg}', desc=self.desc, msg=self.msg)
        else:
            return _(self.desc)


"""
System common exceptions
600 - 999
"""


class UndefinedException(ECloudException):
    desc = 'Undefined common exception'
    code = 600


class InvalidParameters(ECloudException):
    """Invalid parameters from request"""

    desc = 'Invalid Parameters'
    code = 601


class ImproperConfiguration(ECloudException):

    desc = 'Improper configuration'
    code = 602

