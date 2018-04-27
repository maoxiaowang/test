# coding=utf-8
"""
Storage, volume
"""
from django.views.generic import (
    CreateView, UpdateView, DeleteView, ListView, DetailView)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_http_methods
from .models import Volume
# Create your views here.


class VolumeList(ListView, PermissionRequiredMixin):

    permission_required = 'storage.volume_list'
    model = Volume
    template_name = 'storage/volume_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        return {'test': 'hello world'}

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)


@method_decorator(login_required, name='dispatch')
class VolumeDetail(DetailView, PermissionRequiredMixin):

    permission_required = 'storage.volume_detail'
    model = Volume

    def get(self, request, *args, **kwargs):
        pass


@method_decorator(login_required, name='dispatch')
class VolumeCreate(CreateView, PermissionRequiredMixin):

    permission_required = 'storage.volume_create'
    template_name = 'storage/volume_create.html'
    model = Volume

    def get_context_data(self, **kwargs):
        pass

    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        pass


class VolumeUpdate(UpdateView, PermissionRequiredMixin):

    permission_required = 'storage.volume_update'
    model = Volume

    def put(self, *args, **kwargs):
        pass


class VolumeDelete(DeleteView, PermissionRequiredMixin):

    permission_required = 'storage.volume_delete'
    model = Volume

    def delete(self, request, *args, **kwargs):
        pass


