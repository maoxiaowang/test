from django.views.generic import (View, CreateView,
    UpdateView, DeleteView, ListView, DetailView)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.utils.decorators import method_decorator
from cinder.models import Volumes
from storage.tasks import create_volumes
from common.mixin import JSONResponseMixin

# Create your views here.


@method_decorator(login_required, name='dispatch')
class VolumeList(PermissionRequiredMixin, ListView):

    permission_required = 'storage.list_volume'
    raise_exception = True
    model = Volumes
    template_name = 'storage/volume_list.html'

    def get_queryset(self):
        volumes = self.model.objects.filter(deleted=0)
        return volumes


class VolumeDetail(PermissionRequiredMixin, DetailView):

    permission_required = 'storage.detail_volume'
    raise_exception = True
    model = Volumes
    pk_url_kwarg = 'volume_id'
    template_name = 'storage/volume_detail.html'


class VolumeCreate(PermissionRequiredMixin, JSONResponseMixin, View):

    permission_required = 'storage.create_volume'
    raise_exception = True
    model = Volumes

    def post(self, request, *args, **kwargs):
        # TODO: create volume
        create_volumes(request).delay()


class VolumeUpdate(PermissionRequiredMixin, UpdateView):

    permission_required = 'storage.update_volume'
    raise_exception = True
    model = Volumes

    def put(self, *args, **kwargs):
        pass


class VolumeDelete(DeleteView, PermissionRequiredMixin):

    permission_required = 'storage.delete_volume'
    raise_exception = True
    model = Volumes

    def delete(self, request, *args, **kwargs):
        pass
