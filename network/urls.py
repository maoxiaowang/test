# coding=utf-8
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import TemplateView
from django.urls import path, re_path, register_converter
from django.urls.converters import UUIDConverter
from . import views

app_name = 'networks'

register_converter(UUIDConverter, 'uuid')
# <to_url:to_python>

urlpatterns = [
    path('network/', views.NetworkList.as_view(), name='network_list'),
    path('network/detail/<uuid:uuid>/', views.NetworkDetail.as_view(), name='network_detail'),
    path('network/create/', views.NetworkCreate.as_view(), name='network_create'),
]
