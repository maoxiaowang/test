# coding=utf-8
import requests


class OpenStackRequest(object):

    def __init__(self, request):
        """
        :param request: Django request object
        """
        token = request.session.get('os-token')
        headers = {'Content-Type': 'application/json'}
        self.headers = (headers if not token else
                        headers.update({'X-Auth-Token': token}))

    @staticmethod
    def get(url, params=None, **kwargs):
        payload = requests.get(url, params=params, **kwargs)
        return payload

    @staticmethod
    def post(url, data=None, json=None, **kwargs):
        payload = requests.post(url, data=data, json=json, **kwargs)
        return payload

    @staticmethod
    def put(url, data, **kwargs):
        payload = requests.put(url, data=data, **kwargs)
        return payload

    @staticmethod
    def delete(url, **kwargs):
        payload = requests.delete(url, **kwargs)
        return payload
