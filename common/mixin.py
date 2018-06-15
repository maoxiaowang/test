# coding=utf-8
import json

from django.contrib.auth.mixins import AccessMixin
from django.contrib.auth.views import redirect_to_login
from django.db.models.query import QuerySet
from django.http import JsonResponse
from django.utils.translation import ugettext_lazy as _
from django.views.generic.detail import (
    SingleObjectTemplateResponseMixin, BaseDetailView)


def ret_format(result=True, messages=None, level=None, code=0, data=None, default_msg=True):
    """
    格式化Json返回数据
    :param result: bool, 一般为True
    :param messages: str|list, 要在页面展示的消息，多条消息使用列表
    :param level: str，消息级别，
    默认result为True时为success，False时为error
    :param code: 消息代码
    :param data: Json|dict|list|QuerySet, 返回给前端的数据
    :param default_msg: messages为None时，若default_messages开启，返回一条默认消息
    :return: dict
    """
    assert isinstance(result, bool)
    if messages:
        if not isinstance(messages, (list, tuple, str)):
            raise ValueError('messages can only be list, tuple or str')
        if isinstance(messages, str):
            messages = [messages]
        # i18n here
        messages = [_(m) for m in messages]
    else:
        if default_msg:
            messages = [_('Operation succeeded')] if result else [_('Operation failed')]
    if not level:
        level = 'success' if result else 'error'
    assert level in ('success', 'info', 'warning', 'error')
    assert isinstance(code, int)
    if data:
        if isinstance(data, str):
            try:
                data = json.loads(data)
            except json.JSONDecodeError:
                raise ValueError('data is not type of Json, or can not be serialized by JSON')
        if isinstance(data, QuerySet):
            if hasattr(data, '__iter__') and isinstance(data[0], dict):
                data = [item for item in data]

    return {'result': result,
            'messages': messages or [],
            'level': level,
            'code': code,
            'data': data or {}}


class JSONResponseMixin:
    """
    A mixin that can be used to render a JSON response.
    """
    def render_to_json_response(self, result=True, messages=None, level=None,
                                code=0, data=None, default_msg=True,
                                **response_kwargs):
        """
        Returns a JSON response, transforming 'context' to make the payload.
        """
        res_data = self._get_ret_form_data(result=result, messages=messages,
                                           level=level, code=code, data=data,
                                           default_msg=default_msg)
        return JsonResponse(
            res_data,
            **response_kwargs
        )

    def _get_ret_form_data(self, **kwargs):
        """
        Returns an object that will be serialized as JSON by json.dumps().
        """
        # Note: This is *EXTREMELY* naive; in reality, you'll need
        # to do much more complex handling to ensure that arbitrary
        # objects -- such as Django model instances or querysets
        # -- can be serialized as JSON.

        return ret_format(result=kwargs['result'],
                          messages=kwargs['messages'],
                          level=kwargs['level'],
                          code=kwargs['code'],
                          data=kwargs['data'],
                          default_msg=kwargs['default_msg'])


class AjaxableResponseMixin:
    """
    Mixin to add AJAX support to a form.
    Must be used with an object-based FormView (e.g. CreateView)
    """
    def form_invalid(self, form):
        response = super().form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        response = super().form_valid(form)
        if self.request.is_ajax():
            data = {
                'pk': self.object.pk,
            }
            return JsonResponse(data)
        else:
            return response


class HybridDetailView(JSONResponseMixin, SingleObjectTemplateResponseMixin, BaseDetailView):
    def render_to_response(self, context):
        # Look for a 'format=json' GET argument
        if self.request.GET.get('format') == 'json':
            return self.render_to_json_response(context)
        else:
            return super().render_to_response(context)


class LoginRequiredMixin(AccessMixin):
    """Verify that the current user is authenticated."""
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect_to_login(self.request.get_full_path(), self.get_login_url(),
                                     self.get_redirect_field_name())
        return super().dispatch(request, *args, **kwargs)
