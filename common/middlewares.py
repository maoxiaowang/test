"""
Create middleware here, don't forget to add it to the MIDDLEWARE list
in your Django settings.

Reference:
https://docs.djangoproject.com/en/2.0/topics/http/middleware/

"""
# coding=utf-8

from common.exceptions.base import ECloudException
from django.shortcuts import HttpResponse
import json


class CommonMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    def process_view(self, request, view_func, *view_args, **view_kwargs):
        """
        在执行view前调用。
        :param request:
        :return: None or an HttpResponse object
        """
        return None

    def process_exception(self, request, exception):
        """
        当抛出异常时调用。
        :param request:
        :param exception:
        :return:
        """
        if isinstance(exception, ECloudException):
            if request.method in ('POST', 'PUT', 'DELETE'):
                result = dict(result=False, message={}, redirect='', data={})
                result['message'] = {
                        'code': exception.code,
                        'desc': exception.desc,
                        'level': exception.level
                }
                return HttpResponse(json.dumps(result))
            elif request.method == 'GET':
                pass
            else:
                # other HTTP methods
                pass
        else:
            # django or openstack
            pass

    def process_template_response(self, request, response):
        """
        view 执行完毕后调用。
        :param request:
        :param response:
        :return:
        """
        path_info = request.path_info.strip('/').split('/')

        return response
