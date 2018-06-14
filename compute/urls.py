# coding=utf-8
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import TemplateView
from django.urls import path, re_path, register_converter
from compute.views import host, server, snapshot, backup, image
from django.urls.converters import UUIDConverter

app_name = 'compute'
register_converter(UUIDConverter, 'uuid')

urlpatterns = [
    path('server/', login_required(server.ServerList.as_view()), name='server_list'),
    path('server/<uuid:uuid>/', login_required(server.ServerDetail.as_view()), name='server_detail'),

    path('host/', login_required(host.HostList.as_view()), name='host_list'),
    path('host/<uuid:uuid>/', login_required(host.HostDetail.as_view()), name='host_detail'),

    path('snapshot/', login_required(snapshot.SnapshotList.as_view()), name='snap_list'),

    path('image/', login_required(image.ImageList.as_view()), name='image_list'),

    path('backup/', login_required(backup.BackupList.as_view()), name='backup_list'),
]