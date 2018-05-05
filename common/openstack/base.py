# coding=utf-8
import requests
import json
from common.openstack.constants import *
import time


class OpenStackRequest(object):

    def __init__(self, request):
        """
        :param request: Django request object
        """

        token = self.get_token
        self.request = request
        self.headers = {'Content-Type': 'application/json', 'X-Auth-Token': token}

    def __get_token(self):
        # TODO: request token from OpenStack
        params = {}
        try:
            res = self.get(
                'http://%s:%s/v3/auth/token' % (HOST, KEYSTONE_PORT),
                params=params
            )
        except Exception as e:
            # log
            raise e
        headers = res.headers
        return json.loads(headers['x-auth-token'])

    @property
    def get_token(self):
        # get token from django request
        token = self.request.user.get('token')
        if token:
            created_at = token.get('created_at')
            if time.time() - created_at >= OPENSTACK_TOKEN_TIMEOUT:
                return self.__get_token()
            return token
        else:
            return self.__get_token()

    def get(self, url, params=None, **kwargs):

        payload = requests.get(url, params=params, headers=self.headers, **kwargs)
        return payload

    def post(self, url, data=None, json=None, **kwargs):
        payload = requests.post(url, data=data, json=json, headers=self.headers, **kwargs)
        return payload

    def put(self, url, data=None, **kwargs):
        payload = requests.put(url, data=data, headers=self.headers, **kwargs)
        return payload

    def delete(self, url, **kwargs):
        payload = requests.delete(url, headers=self.headers, **kwargs)
        return payload
