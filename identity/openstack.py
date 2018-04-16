# coding=utf-8
from common.openstack.base import OpenStackRequest


class IdentityRequest(OpenStackRequest):

    def auth_token(self, username, password, version=3):
        """
        Login to OpenStack.
        We don't use keystone system, so we can hard code here
        :param username:
        :param password:
        :param version:
        :return:
        """
        pass
