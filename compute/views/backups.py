# coding=utf-8
from django.views.generic import (ListView, DetailView, CreateView,
                                  UpdateView, DeleteView)


class BackupList(ListView):
    pass


class BackupDetail(DetailView):
    pass


class BackupCreate(CreateView):
    pass


class BackupUpdate(UpdateView):
    pass


class BackupDelete(DeleteView):
    pass
