from .base import OpenStackRequest


class CinderRequest(OpenStackRequest):

    def get_volumes(self):
        # fixme: should replace by real OpenStack API
        pass

    def create_volumes(self):
        pass