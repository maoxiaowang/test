"""
Exceptions for alarm

codes: 12000 - 12999
"""
# coding=utf-8

from common.exceptions import ECloudException


class Example(ECloudException):
    level = 'error'
    desc = 'I am an example'
    code = 12000
