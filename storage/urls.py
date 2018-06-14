# coding=utf-8
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import TemplateView
from django.urls import path, re_path, register_converter
from django.urls.converters import UUIDConverter
from storage.views import volume, storage

app_name = 'storage'

register_converter(UUIDConverter, 'uuid')
# <to_url:to_python>

urlpatterns = [
    path('volume/', volume.VolumeList.as_view(), name='volume_list'),
    path('volume/detail/<uuid:volume_id>/', volume.VolumeDetail.as_view(), name='volume_detail'),
    path('volume/create/', volume.VolumeCreate.as_view(), name='volume_create'),
    path('volume/update/<uuid:volume_id>/', volume.VolumeUpdate.as_view(), name='volume_update'),
    path('volume/delete/<uuid:volume_id>/', volume.VolumeDelete.as_view(), name='volume_delete'),

    path('storage/', storage.StorageList.as_view(), name='storage_list'),
    path('storage/detail/<uuid:storage_id>/', storage.StorageDetail.as_view(), name='storage_detail'),
    path('storage/create/', storage.StorageCreate.as_view(), name='storage_create'),

]