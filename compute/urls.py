# coding=utf-8
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import TemplateView
from django.urls import path, re_path, register_converter
from compute.views import host, server, snapshot, backup, image
from django.urls.converters import UUIDConverter

app_name = 'compute'
register_converter(UUIDConverter, 'uuid')

urlpatterns = [
    path('server/', server.ServerList.as_view(), name='server_list'),
    path('server/detail/<uuid:uuid>/', server.ServerDetail.as_view(), name='server_detail'),
    path('server/create/', login_required(server.ServerCreate.as_view()), name='server_create'),

    path('host/', host.HostList.as_view(), name='host_list'),
    path('host/detail/<uuid:uuid>/', host.HostDetail.as_view(), name='host_detail'),
    path('host/create/', host.HostCreate.as_view(), name='host_create'),

    path('snapshot/', snapshot.SnapshotList.as_view(), name='snap_list'),
    path('snapshot/detail/<uuid:uuid>/', snapshot.SnapshotDetail.as_view(), name='snapshot_detail'),
    path('snapshot/create/', snapshot.SnapshotCreate.as_view(), name='snapshot_create'),

    path('image/', image.ImageList.as_view(), name='image_list'),
    path('image/detail/<uuid:uuid>/', image.ImageDetail.as_view(), name='image_detail'),
    path('image/create/', image.ImageCreate.as_view(), name='image_create'),

    path('backup/', backup.BackupList.as_view(), name='backup_list'),
    path('backup/detail/<uuid:uuid>/', backup.BackupDetail.as_view(), name='backup_detail'),
    path('backup/create/', backup.BackupCreate.as_view(), name='backup_create'),
]