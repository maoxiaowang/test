# coding=utf-8
import requests
import json
from common.exceptions import ImproperConfiguration
from common.log import Logging
from django.conf import settings
import time


Log = Logging.default_logger


class OpenStackRequest(object):

    def __init__(self, request):
        """
        :param request: Django request object
        """

        token = self.get_token
        self.request = request
        self.headers = {'Content-Type': 'application/json', 'X-Auth-Token': token}
        try:
            keystone = settings.OPENSTACK['keystone']
            self._user = keystone['user']
            self._pass = keystone['pass']
            self._host = keystone['host']
            self._port = keystone['port']
            self._timeout = keystone['token_timeout']
            assert all((self._user, self._host, self._port, self._timeout))
            assert isinstance(self._port, int)
            assert isinstance(self._timeout, int)
        except (KeyError, AssertionError) as e:
            raise ImproperConfiguration(str(e))

    def __get_token(self):
        # TODO: request token from OpenStack
        params = {
            "auth": {
                "identity": {
                    "methods": [
                        "password"
                    ],
                    "password": {
                        "user": {
                            "name": "admin",
                            "domain": {
                                "name": self._user
                            },
                            "password": self._pass
                        }
                    }
                }
            }
        }
        try:
            res = self.post(
                'http://%s:%s/v3/auth/token' % (self._host, self._port),
                params=params
            )
        except Exception as e:
            Log.debug('Request token from keystone error: %s' % str(e))
            raise e
        headers = res.headers
        return json.loads(headers['x-auth-token'])

    @property
    def get_token(self):
        # get token from django request
        token = self.request.user.get('token')
        if token:
            created_at = token.get('created_at')
            if time.time() - created_at >= self._timeout:
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
