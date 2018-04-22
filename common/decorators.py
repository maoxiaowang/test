# coding=utf-8
"""

"""
from django.http import Http404, HttpResponseForbidden
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test


def request_method(method):
    """
    A decoration to ensure the request run in a designated way.
    You need pass a string argument in 'POST', 'GET', 'PUT', 'DELETE'
    All methods are 'get', 'post', 'put', 'patch', 'delete', 'head',
        'options', 'trace'
    """
    method = method.upper()
    methods = ('POST', 'GET', 'PUT', 'DELETE',
               'HEAD', 'PATCH', 'OPTIONS', 'TRACE')
    if method not in methods:
        raise HttpResponseForbidden

    def wrapper(func):
        def method_filter(request, *args, **kwargs):
            if request.method == method:
                return func(request, *args, **kwargs)
            else:
                raise Http404
        return method_filter
    return wrapper


def login_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url=None):
    """
    Decorator for views that checks that the user is logged in, redirecting
    to the log-in page if necessary.
    """
    actual_decorator = user_passes_test(
        lambda u: u.is_authenticated,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator