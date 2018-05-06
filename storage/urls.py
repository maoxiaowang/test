# coding=utf-8
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import TemplateView
from django.urls import path, re_path, register_converter
from django.urls.converters import UUIDConverter
from . import views

app_name = 'storage'

register_converter(UUIDConverter, 'uuid')
# <to_url:to_python>

urlpatterns = [
    path('volume/', views.VolumeList.as_view(), name='volume_list'),
    path('volume/detail/<uuid:volume_id>', views.VolumeDetail.as_view(),
         name='volume_detail'),
    path('volume/create/', views.VolumeCreate.as_view(), name='volume_create'),
    path('volume/update/', views.VolumeUpdate.as_view(), name='volume_update'),
    path('volume/delete/', views.VolumeDelete.as_view(), name='volume_delete'),
    path('storage/', views.StorageList.as_view(), name='storage_list')
]