# coding=utf-8
import logging

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import ListView

from identity.models import Permission

logger = logging.getLogger('default')


# Create your views here.


class PermissionList(PermissionRequiredMixin, ListView):

    permission_required = 'identity.list_permission'
    model = Permission
    template_name = 'identity/management/permission_list.html'
