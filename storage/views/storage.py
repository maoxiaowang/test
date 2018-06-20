# coding=utf-8
from django.views.generic import (ListView, DetailView, CreateView,
                                  UpdateView, DeleteView)
from django.contrib.auth.mixins import PermissionRequiredMixin
from common.mixin import LoginRequiredMixin
from common.constants.resources import STORAGE


class StorageList(LoginRequiredMixin, PermissionRequiredMixin, ListView):

    permission_required = 'storage.storage_list'
    raise_exception = True

    context_object_name = 'storage_list'
    template_name = 'storage/storage/storage_list.html'

    def get_queryset(self):
        self.queryset = self.request.user.get_resources_by_type(resource_type=STORAGE,
                                                                detail=True)
        return super().get_queryset()


class StorageDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    pass


class StorageCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    pass


class StorageUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    pass


class StorageDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    pass
