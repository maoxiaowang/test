# coding=utf-8
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import TemplateView
from django.urls import path, re_path, register_converter
from django.urls.converters import UUIDConverter
from . import views

app_name = 'settings'

register_converter(UUIDConverter, 'uuid')
# <to_url:to_python>

urlpatterns = [
    path('', views.SettingsList.as_view(), name='settings_list'),
]
