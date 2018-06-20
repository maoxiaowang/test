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


class ECloudException(Exception):
    # Base view exception
    # level: error, warning, info
    level = 'error'
    desc = 'Undefined exception'
    code = 0

    def __init__(self, msg=None):
        self.msg = msg

    def __str__(self):
        return '%s: %s' % (self.desc, str(self.msg)) \
            if self.msg else self.desc


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

