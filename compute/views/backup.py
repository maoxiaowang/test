# coding=utf-8
from django.views.generic import (ListView, DetailView, CreateView,
                                  UpdateView, DeleteView)
from django.contrib.auth.mixins import PermissionRequiredMixin
from common.mixin import LoginRequiredMixin
from common.constants.resources import BACKUP


class BackupList(LoginRequiredMixin, PermissionRequiredMixin, ListView):

    permission_required = 'compute.list_backup'
    raise_exception = True

    context_object_name = 'backup_list'
    template_name = 'compute/backup/backup_list.html'

    def get_queryset(self):
        self.queryset = self.request.user.get_resources_by_type(resource_type=BACKUP)
        return super().get_queryset()


class BackupDetail(DetailView):
    pass


class BackupCreate(CreateView):
    pass


class BackupUpdate(UpdateView):
    pass


class BackupDelete(DeleteView):
    pass
