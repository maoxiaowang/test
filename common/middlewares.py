"""
Create middleware here, don't forget to add it to the MIDDLEWARE list
in your Django settings.

Reference:
https://docs.djangoproject.com/en/2.0/topics/http/middleware/

"""
# coding=utf-8

from common.exceptions import ECloudException
from django.shortcuts import HttpResponse
import json
from django.utils.deprecation import MiddlewareMixin


class CommonMiddleware(MiddlewareMixin):

    def __init__(self, get_response):
        # self.get_response = get_response
        super().__init__(get_response)
        # One-time configuration and initialization.
        from dashboard.models import Menu
        menus = Menu.objects.all()
        self.menus_obj = menus
        self.menus_list = [item.name for item in menus]

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        response = self.get_response(request)
        #
        # # Code to be executed for each request/response after
        # # the view is called.
        #
        return response

    # def process_view(self, request, view_func, *view_args, **view_kwargs):
    #     """
    #     在执行view前调用。
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

    # def process_request(self, request):
    #     return request
    #
    # def process_response(self, request, response):
    #     path = request.path_info.strip('/').split('/')
    #     response = self.get_response(request)
    #     path_len = len(path)
    #     if path[0] in self.menus_list:
    #         if not hasattr(response, 'context_data'):
    #             response.context_data = {}
    #         response.context_data['side_nav_menus'] = self.menus_obj
    #     return response

    def process_template_response(self, request, response):
        """
        view 执行完毕后调用。
        view返回对象必须包含render方法，如django.template.response.TemplateResponse
        :param request:
        :param response:
        :return:
        """
        path = request.path_info.strip('/').split('/')
        path_len = len(path)
        if path[0] in self.menus_list:
            print(self.menus_list)
            if not response.context_data:
                response.context_data = {}
            response.context_data['side_nav_menus'] = self.menus_obj
            # if path_len == 1:
            #     # no submenu
            #     menu = None
            #     for item in self.menus_obj:
            #         if item['region'].address == menu_name:
            #             menu = item
            #             response.context_data['current_region'] = menu['region']
            #     if path_len > 2:
            #         board_address = path[2]
            #         if menu :
            #             # if there is any sub menu
            #             for board in menu.get('boards', []):
            #                 if board.address == board_address:
            #                     response.context_data['current_board'] = board
            # elif path_len == 2:
            #     pass
            # else:
            #     raise ValueError
        return response

