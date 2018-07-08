from django.shortcuts import render
from django.views.generic import (
    CreateView, UpdateView, DeleteView, ListView, DetailView)
from django.contrib.auth.mixins import PermissionRequiredMixin
from common.mixin import LoginRequiredMixin

# Create your views here.


class SettingsList(LoginRequiredMixin, PermissionRequiredMixin, ListView):

    template_name = 'settings/settings_list.html'
    permission_required = 'settings.list_settings'

    def get_queryset(self):
        pass
