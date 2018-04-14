# coding=utf-8
"""
Exceptions codes:
1 - 999: common
1000 - 1999:   compute
2000 - 2999:   volumes
3000 - 3999:   hosts
4000 - 4999:   networks
5000 - 5999:   storage
6000 - 6999:   snapshots
7000 - 7999:   meters
8000 - 8999:   images
9000 - 9999:   security
10000 - 10999: identity
11000 - 11999: backup
12000 - 12999: alarms
13000 - 13999: reports
14000 - 14999: orders

Exceptions level:
error, warning, info, default

Exceptions desc:
short and accurate description for an exception
"""
from django.utils.translation import ugettext_lazy as _


class ECloudException(Exception):
    # Base view exception
    # level: error, warning, info, default
    level = 'error'
    desc = _('Undefined exception')
    code = 0


"""
System common exceptions
1 - 999
"""


class UndefinedException(ECloudException):
    desc = _('Undefined common exception')
    code = 1


class EmptyContent(ECloudException):
    level = 'warning'
    desc = _('Empty content is not allowed')
    code = 2


class InvalidParameters(ECloudException):
    desc = _('Invalid Parameters')
    code = 3
