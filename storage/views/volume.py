from django.views.generic import (View, CreateView,
                                  UpdateView, DeleteView, ListView, DetailView)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.utils.decorators import method_decorator
from storage.tasks import create_volumes
from common.mixin import JSONResponseMixin
from common.constants.resources import VOLUME
from storage.models.cinder import Volumes

# Create your views here.


@method_decorator(login_required, name='dispatch')
class VolumeList(PermissionRequiredMixin, ListView):

    permission_required = 'resource.list_volume'
    raise_exception = True

    context_object_name = 'volume_list'
    template_name = 'storage/volume/volume_list.html'

    def get_queryset(self):
        user_resources = self.request.user.get_resources(resource_type=VOLUME)
        resource_ids = [item.id for item in user_resources]
        self.queryset = Volumes.objects.filter(id__in=resource_ids, deleted=0)
        return super().get_queryset()


class VolumeDetail(PermissionRequiredMixin, DetailView):

    permission_required = 'resource.detail_volume'
    raise_exception = True

    pk_url_kwarg = 'volume_id'
    template_name = 'storage/volume/volume_detail.html'


class VolumeCreate(PermissionRequiredMixin, JSONResponseMixin, View):

    permission_required = 'resource.create_volume'
    raise_exception = True

    def post(self, request, *args, **kwargs):
        # TODO: create volume
        create_volumes(request).delay()


class VolumeUpdate(PermissionRequiredMixin, UpdateView):

    permission_required = 'resource.update_volume'
    raise_exception = True

    def put(self, *args, **kwargs):
        pass


class VolumeDelete(DeleteView, PermissionRequiredMixin):

    permission_required = 'resource.delete_volume'
    raise_exception = True

    def delete(self, request, *args, **kwargs):
        pass
