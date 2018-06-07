# coding=utf-8
from django.views.generic import (ListView, DetailView, CreateView, 
                                  UpdateView, DeleteView)
from common.constants.resources import SERVER
from django.contrib.auth.mixins import PermissionRequiredMixin


class ServerList(PermissionRequiredMixin, ListView):

    permission_required = 'compute.list_server'
    raise_exception = True

    context_object_name = 'server_list'
    template_name = 'compute/server/server_list.html'

    def get_queryset(self):
        self.queryset = self.request.user.get_resources(resource_type=SERVER)
        return super().get_queryset()


class ServerDetail(DetailView):
    pass


class ServerAdd(CreateView):
    pass


class ServerUpdate(UpdateView):
    pass


class ServerRemove(DeleteView):
    pass
