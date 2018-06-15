# coding=utf-8
from django.views.generic import (ListView, DetailView, CreateView,
                                  UpdateView, DeleteView)
from django.contrib.auth.mixins import PermissionRequiredMixin
from common.mixin import LoginRequiredMixin
from common.constants.resources import IMAGE


class ImageList(LoginRequiredMixin, PermissionRequiredMixin, ListView):

    permission_required = 'compute.list_image'
    raise_exception = True

    context_object_name = 'image_list'
    template_name = 'compute/image/image_list.html'

    def get_queryset(self):
        self.queryset = self.request.user.get_resources_by_type(resource_type=IMAGE)
        return super().get_queryset()


class ImageDetail(DetailView):
    pass


class ImageCreate(CreateView):
    pass


class ImageUpdate(UpdateView):
    pass


class ImageDelete(DeleteView):
    pass
