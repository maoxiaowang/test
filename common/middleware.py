"""
Create middleware here, don't forget to add it to the MIDDLEWARE list
in your Django settings.

Reference:
https://docs.djangoproject.com/en/2.0/topics/http/middleware/

"""
# coding=utf-8

import sys

from django.conf import settings
from django.core.exceptions import PermissionDenied
from django.http.response import JsonResponse
from django.utils.deprecation import MiddlewareMixin
from django.views.debug import technical_500_response

from common.exceptions import ECloudException
from common.mixin import ret_format


class CommonMiddleware(MiddlewareMixin):

    def __init__(self, get_response):
        # self.get_response = get_response
        super().__init__(get_response)
        # One-time configuration and initialization.

        # Initialize first starting of the system

    # def __call__(self, request):
    #     # Code to be executed for each request before
    #     # the view (and later middleware) are called.
    #     super().__call__(request)
    #     response = self.get_response(request)
    #
    #     # Code to be executed for each request/response after
    #     # the view is called.
    #
    #     return response

    # def process_view(self, request, view_func, *view_args, **view_kwargs):
    #     """
    #     call before view executing
    #     :param request:
    #     :return: None or an HttpResponse object
    #     """
    #     return None

    def process_exception(self, request, exception):
        """
        当抛出异常时调用。
        :param request:
        :param exception:
        :return:
        """
        if isinstance(exception, ECloudException):
            if request.method in ('POST', 'PUT', 'DELETE'):

                return JsonResponse(
                    ret_format(result=False, messages=exception.desc,
                               level=exception.level, code=exception.code))
            elif request.method == 'GET':
                pass
            else:
                # other HTTP methods
                pass
        else:
            # django or openstack exceptions
            if request.method in ('POST', 'PUT', 'DELETE'):
                code = 0
                level = None
                data = None
                if isinstance(exception, PermissionDenied):
                    messages = "You don't have permission to do this"
                    level = 'warning'
                    code = 403
                else:
                    messages = str(exception)

                return JsonResponse(
                    ret_format(result=False, messages=messages,
                               code=code, level=level, data=data)
                )
    # def process_request(self, request):
    #     return request

    # def process_response(self, request, response):
    #     path = request.path_info.strip('/').split('/')
    #     response = self.get_response(request)
    #     if not hasattr(response, 'context_data'):
    #         response.context_data = {}
    #     bc = list()
    #     for i in range(len(path)):
    #         bc.append({'path': '/%s/' % '/'.join(path[:i + 1]),
    #                    'name': path[i].capitalize()})
    #     response.context_data['breadcrumb_paths'] = bc
    #     return response

    def process_template_response(self, request, response):
        """
        call after view finished
        objects returned by view must contain render method, such as
        django.template.response.TemplateResponse
        :param request:
        :param response:
        :return:
        """
        path = request.path_info.strip('/').split('/')

        if not response.context_data:
            response.context_data = {}
        # add menu
        # response.context_data['side_nav_menus'] = self.menus_obj

        # add breadcrumb
        bc = list()
        for i in range(len(path)):
            bc.append({'path': '/%s/' % '/'.join(path[:i + 1]),
                       'name': path[i].capitalize()})
        response.context_data['breadcrumb_paths'] = bc

        return response


class UserBasedExceptionMiddleware(MiddlewareMixin):
    """
    Let superuser see debug page when exception happens
    """

    def process_exception(self, request, exception):
        if request.user.is_superuser or request.META.get('REMOTE_ADDR') in settings.INTERNAL_IPS:
            return technical_500_response(request, *sys.exc_info())
