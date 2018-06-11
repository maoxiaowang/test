# coding=utf-8
from django.views.generic import (ListView, DetailView, CreateView, 
                                  UpdateView, DeleteView)


class ServerList(ListView):
    pass


class ServerDetail(DetailView):
    pass


class ServerAdd(CreateView):
    pass


class ServerUpdate(UpdateView):
    pass


class ServerRemove(DeleteView):
    pass
