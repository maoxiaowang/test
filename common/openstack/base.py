# coding=utf-8
import requests
import json
from common.exceptions import ImproperConfiguration
from common.log import Logging
from django.conf import settings
import time


Log = Logging.default_logger


SERVICE_TYPES = {
    'nova': 8774,
    'cinder': 8776,
    'keystone': 5000,
    'neutron': 9696
}


class OpenStackRequest(object):

    connect_timeout, read_timeout = 5.0, 30.0
    timeout = (connect_timeout, read_timeout)

    def __init__(self, service_type):
        """
        :param service_type: OpenStack service types
        """
        assert service_type.lower() in [_ for _ in SERVICE_TYPES]
        self.service_type = service_type

        try:
            ks = settings.OPENSTACK['keystone']
            self.ks_user = ks['user']
            self.ks_pass = ks['pass']
            self.ks_host = ks['host']
            self.ks_port = ks['port']
            self.ks_timeout = ks['token_timeout']
            self.ks_project_id = ks['project_id']
            assert all((self.ks_user, self.ks_pass, self.ks_host,
                        self.ks_port, self.ks_timeout))
            assert isinstance(self.ks_port, int)
            assert isinstance(self.ks_timeout, int)
        except (KeyError, AssertionError) as e:
            raise ImproperConfiguration(str(e))

    def _get_token(self):
        # TODO: request token from OpenStack
        params = {
            "auth": {
                "identity": {
                    "methods": [
                        "password"
                    ],
                    "password": {
                        "user": {
                            "name": self.ks_user,
                            "domain": {
                                "name": 'default'
                            },
                            "password": self.ks_pass
                        }
                    }
                }
            }
        }
        try:
            res = self.post(
                None,
                'http://%s:%s/v3/auth/token' % (self.ks_host, self.ks_port),
                params=params
            )
        except Exception as e:
            Log.debug('Request token from keystone error: %s' % str(e))
            raise e
        headers = res.headers
        return json.loads(headers['x-subject-token'])

    def get_token(self, request):
        # get token from django request
        # {'id': '', 'created_at': ''}
        token = request.user.get('token')
        if token:
            created_at = token['created_at']
            if time.time() - created_at >= self.ks_timeout:
                return self._get_token()
            return token['id']
        else:
            return self._get_token()

    def _get_header(self, request):
        if request is not None:
            return {'Content-Type': 'application/json',
                    'X-Auth-Token': self.get_token(request)}
        else:
            return {'Content-Type': 'application/json'}

    def _fill(self, url):
        if not url.startswith('/'):
            raise ValueError('URL should start with "/", '
                             'e.g. /v3/{project_id}/volumes')
        return 'http://%s:%d' % (self.ks_host, SERVICE_TYPES[self.service_type]) + url

    def get(self, request, url, params=None, **kwargs):
        payload = requests.get(self._fill(url), params=params, timeout=self.timeout,
                               headers=self._get_header(request), **kwargs)
        return payload

    def post(self, request, url, data=None, json=None, **kwargs):
        payload = requests.post(self._fill(url), data=data, json=json, timeout=self.timeout,
                                headers=self._get_header(request), **kwargs)
        return payload

    def put(self, request, url, data=None, **kwargs):
        payload = requests.put(self._fill(url), data=data, timeout=self.timeout,
                               headers=self._get_header(request), **kwargs)
        return payload

    def delete(self, request, url, **kwargs):
        payload = requests.delete(self._fill(url), timeout=self.timeout,
                                  headers=self._get_header(request), **kwargs)
        return payload
