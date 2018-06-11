# coding=utf-8
from django.views.generic import (ListView, DetailView, CreateView,
                                  UpdateView, DeleteView)


class HostList(ListView):
    pass


class HostDetail(DetailView):
    pass


class HostAdd(CreateView):
    pass


class HostUpdate(UpdateView):
    pass


class HostRemove(DeleteView):
    pass
