# coding=utf-8
"""

"""
from common.openstack import OpenStackRequest


class ComputeRequest(OpenStackRequest):

    def __init__(self, request):
        super().__init__(request)

    def compute_list(self):
        pass

    def compute_detail(self):
        pass

    def compute_create(self):
        pass

    def compute_delete(self):
        pass