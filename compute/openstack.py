# coding=utf-8
"""

"""
from common.openstack.base import OpenStackRequest


class ComputeRequest(OpenStackRequest):

    def __init__(self, request):
        super().__init__(request)

    def compute_list(self):
        pass

    def compute_detail(self):
        pass

    def compute_create(self, name):
        pass

    def compute_delete(self):
        pass