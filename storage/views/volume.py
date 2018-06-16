from django.views.generic import (View, CreateView, FormView,
                                  UpdateView, DeleteView, ListView, DetailView)
from django.contrib.auth.mixins import PermissionRequiredMixin
# from django.utils.decorators import method_decorator
from storage.tasks import create_volumes
from common.mixin import JSONResponseMixin, LoginRequiredMixin
from common.constants.resources import VOLUME, STORAGE
from django.contrib.auth import get_user_model
from common.models.utils import get_resource_model
from storage.forms.volume import VolumeCreationForm
from common.forms.utils import DivErrorList

User = get_user_model()

# Create your views here.


class VolumeList(LoginRequiredMixin, PermissionRequiredMixin, ListView):

    permission_required = 'storage.list_volume'
    raise_exception = True

    context_object_name = 'volume_list'
    template_name = 'storage/volume/volume_list.html'

    def get_queryset(self):
        self.queryset = self.request.user.get_resources_by_type(
            resource_type=VOLUME, detail=True)
        return super().get_queryset()


class VolumeDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):

    permission_required = 'storage.detail_volume'
    raise_exception = True

    pk_url_kwarg = 'volume_id'
    template_name = 'storage/volume/volume_detail.html'


class VolumeCreate(LoginRequiredMixin, PermissionRequiredMixin, JSONResponseMixin,
                   CreateView):

    permission_required = 'storage.create_volume'
    raise_exception = True

    template_name = 'storage/volume/volume_create.html'
    form_class = VolumeCreationForm

    def get_context_data(self, **kwargs):
        storage = self.request.user.get_resources_by_type(resource_type=STORAGE,
                                                          detail=True)
        users = User.objects.all()
        form = self.form_class(error_class=DivErrorList)
        form.fields['user'].choices = [(u.id, u.username) for u in users]
        form.fields['storage'].choices = [(s.id, s.name) for s in storage ]
        kwargs.update({'form': form})

        return super().get_context_data(**kwargs)

    def post(self, request, *args, **kwargs):
        # TODO: create volume
        create_volumes(request).delay()


class VolumeUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):

    permission_required = 'storage.update_volume'
    raise_exception = True

    def post(self, request, *args, **kwargs):
        pass


class VolumeDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):

    permission_required = 'storage.delete_volume'
    raise_exception = True

    def delete(self, request, *args, **kwargs):
        pass
