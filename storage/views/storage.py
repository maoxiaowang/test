# coding=utf-8
from django.views.generic import (ListView, DetailView, CreateView,
                                  UpdateView, DeleteView)


class StorageList(ListView):
    pass


class StorageDetail(DetailView):
    pass


class StorageCreate(CreateView):
    pass


class StorageUpdate(UpdateView):
    pass


class StorageDelete(DeleteView):
    pass
