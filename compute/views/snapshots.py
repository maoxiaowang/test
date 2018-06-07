# coding=utf-8
from django.views.generic import (ListView, DetailView, CreateView,
                                  UpdateView, DeleteView)


class SnapshotList(ListView):
    pass


class SnapshotDetail(DetailView):
    pass


class SnapshotCreate(CreateView):
    pass


class SnapshotUpdate(UpdateView):
    pass


class SnapshotDelete(DeleteView):
    pass
