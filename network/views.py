from django.shortcuts import render
from django.views.generic import (
    CreateView, UpdateView, DeleteView, ListView, DetailView)
from django.contrib.auth.mixins import PermissionRequiredMixin
from common.constants.resources import NETWORK

# Create your views here.


class NetworkList(ListView, PermissionRequiredMixin):

    permission_required = 'network.list_network'
    raise_exception = True

    context_object_name = 'network_list'
    template_name = 'network/network_list.html'

    def get_queryset(self):
        self.queryset = self.request.user.get_resources(resource_type=NETWORK)
        return super().get_queryset()


class SubNetworkList(ListView, PermissionRequiredMixin):
    pass
