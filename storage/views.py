# coding=utf-8
"""
Storage, volume
"""
from django.views.generic import (
    CreateView, UpdateView, DeleteView, ListView, DetailView, View)
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.utils.decorators import method_decorator
from cinder.models import Volumes
# Create your views here.


@method_decorator(login_required, name='dispatch')
class VolumeList(PermissionRequiredMixin, ListView):

    permission_required = 'storage.list_volume'
    raise_exception = True
    model = Volumes
    template_name = 'storage/volume_list.html'
    # context_object_name = ''  # default will be volume_list
    # ordering = ''

    def get_queryset(self):
        volumes = self.model.objects.all()
        return volumes


class VolumeDetail(PermissionRequiredMixin, DetailView):

    permission_required = 'storage.detail_volume'
    model = Volumes
    template_name = 'storage/volume_detail.html'

    def get(self, request, *args, **kwargs):
        pass


class VolumeCreate(PermissionRequiredMixin, CreateView):

    permission_required = 'storage.create_volume'
    template_name = 'storage/volume_create.html'
    model = Volumes

    def get_context_data(self, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        pass


class VolumeUpdate(PermissionRequiredMixin, UpdateView):

    permission_required = 'storage.update_volume'
    model = Volumes

    def put(self, *args, **kwargs):
        pass


class VolumeDelete(DeleteView, PermissionRequiredMixin):

    permission_required = 'storage.delete_volume'
    model = Volumes

    def delete(self, request, *args, **kwargs):
        pass


class StorageList(ListView):
    pass
