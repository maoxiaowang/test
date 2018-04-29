from django.shortcuts import render
from django.views.generic import (
    CreateView, UpdateView, DeleteView, ListView, DetailView)
from django.contrib.auth.mixins import PermissionRequiredMixin

# Create your views here.


class NetworkList(ListView, PermissionRequiredMixin):
    pass


class SubNetworkList(ListView, PermissionRequiredMixin):
    pass
