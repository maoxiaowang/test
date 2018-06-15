# coding=utf-8
from django.views.generic import (ListView, DetailView, CreateView,
                                  UpdateView, DeleteView)
from django.contrib.auth.mixins import PermissionRequiredMixin
from common.mixin import LoginRequiredMixin
from common.constants.resources import SNAPSHOT


class SnapshotList(LoginRequiredMixin, PermissionRequiredMixin, ListView):

    permission_required = 'compute.list_snapshot'
    raise_exception = True

    context_object_name = 'snapshot_list'
    template_name = 'compute/snapshot/snapshot_list.html'

    def get_queryset(self):
        self.queryset = self.request.user.get_resources_by_type(resource_type=SNAPSHOT)
        return super().get_queryset()


class SnapshotDetail(DetailView):
    pass


class SnapshotCreate(CreateView):
    pass


class SnapshotUpdate(UpdateView):
    pass


class SnapshotDelete(DeleteView):
    pass
