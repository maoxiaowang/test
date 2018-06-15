# coding=utf-8
from django.views.generic import (ListView, DetailView, CreateView,
                                  UpdateView, DeleteView)
from common.constants.resources import HOST
from django.contrib.auth.mixins import PermissionRequiredMixin
from common.mixin import LoginRequiredMixin


class HostList(LoginRequiredMixin, PermissionRequiredMixin, ListView):

    permission_required = 'compute.list_host'
    raise_exception = True

    context_object_name = 'host_list'
    template_name = 'compute/host/host_list.html'

    def get_queryset(self):
        self.queryset = self.request.user.get_resources_by_type(resource_type=HOST)
        return super().get_queryset()


class HostDetail(PermissionRequiredMixin, DetailView):
    pass


class HostCreate(PermissionRequiredMixin, CreateView):
    pass


class HostUpdate(PermissionRequiredMixin, UpdateView):
    pass


class HostRemove(PermissionRequiredMixin, DeleteView):
    pass
