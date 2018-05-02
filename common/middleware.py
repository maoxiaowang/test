"""
Create middleware here, don't forget to add it to the MIDDLEWARE list
in your Django settings.

Reference:
https://docs.djangoproject.com/en/2.0/topics/http/middleware/

"""
# coding=utf-8

from common.exceptions import ECloudException
from .views_helper import ret_format
from django.http.response import JsonResponse, HttpResponse
from django.utils.deprecation import MiddlewareMixin
from django.core.exceptions import PermissionDenied
from django.utils.translation import ugettext_lazy as _


class CommonMiddleware(MiddlewareMixin):

    def __init__(self, get_response):
        # self.get_response = get_response
        super().__init__(get_response)
        # One-time configuration and initialization.

        # from dashboard.models import Menu
        # menus = Menu.objects.all()
        # self.menus_obj = menus
        # self.menus_list = [item.name for item in menus]

        # Initialize admin user if it does not been created,
        # And give all permissions to admin.
        # TODO:

        # create initial users
        from django.contrib.auth import get_user_model
        user_model = get_user_model()
        if not user_model.objects.filter(username='admin'):
            user_model().create_superuser('admin',
                                          email='admin@example.com',
                                          password='password')

        # add extra permissions
        from django.contrib.auth.models import Permission
        perms = [
            ('permission', 'list_permission', 'Can list permission'),
            ('permission', 'detail_permission', 'Can detail permission'),
            ('group', 'list_group', 'Can list group'),
            ('group', 'detail_group', 'Can detail group')]
        for item in perms:
            model_name, code_name, name = item[0], item[1], item[2]
            Permission.objects.get_or_create(name=name,
                                             codename=code_name,
                                             content_type_id=2)


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
                data = {'code': exception.code,
                        'desc': exception.desc,
                        'level': exception.level
                }
                return JsonResponse(ret_format(result=False, data=data))
            elif request.method == 'GET':
                pass
            else:
                # other HTTP methods
                pass
        else:
            # django or openstack exceptions
            if isinstance(exception, PermissionDenied):
                if request.method in ('POST', 'PUT', 'DELETE'):
                    data = {
                        'code': 403,
                        'desc': _("You don't have permission to do this"),
                        'level': 'error'
                    }
                    return JsonResponse(ret_format(result=False, data=data))
    # def process_request(self, request):
    #     return request

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

