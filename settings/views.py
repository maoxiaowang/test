from django.shortcuts import render
from django.views.generic import (
    CreateView, UpdateView, DeleteView, ListView, DetailView)
from django.contrib.auth.mixins import PermissionRequiredMixin

# Create your views here.


class SettingsList(ListView, PermissionRequiredMixin):

    template_name = 'settings/settings_list.html'

    def get_queryset(self):
        pass
