# coding=utf-8
import logging

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from identity.models import Permission


# Create your views here.


@method_decorator(login_required, name='dispatch')
class PermissionList(PermissionRequiredMixin, ListView):

    permission_required = 'identity.list_permission'
    raise_exception = True
    model = Permission
    template_name = 'identity/management/permission_list.html'
