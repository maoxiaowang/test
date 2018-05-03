# coding=utf-8
"""
Exceptions codes:
1 - 599: Http
600 - 999: common


Exceptions level:
error, warning, info

Exceptions desc:
short and accurate description for an exception
"""


class ECloudException(Exception):
    # Base view exception
    # level: error, warning, info
    level = 'error'
    desc = 'Undefined exception'
    code = 0


"""
System common exceptions
600 - 999
"""


class UndefinedException(ECloudException):
    desc = 'Undefined common exception'
    code = 600


class InvalidParameters(ECloudException):
    desc = 'Invalid Parameters'
    code = 601
