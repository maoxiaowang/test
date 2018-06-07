# coding=utf-8
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import TemplateView
from django.urls import path, re_path, register_converter
from compute.views import hosts, servers, snapshots, backups, images
from django.urls.converters import UUIDConverter

app_name = 'compute'
register_converter(UUIDConverter, 'uuid')

urlpatterns = [
    path('server/', login_required(servers.ServerList.as_view()), name='server_list'),
    path('server/<uuid:uuid>/', login_required(servers.ServerDetail.as_view()), name='server_detail'),

    path('host/', login_required(hosts.HostList.as_view()), name='host_list'),
    path('host/<uuid:uuid>/', login_required(hosts.HostDetail.as_view()), name='host_detail'),

    path('snapshot/', login_required(snapshots.SnapshotList.as_view()), name='snap_list'),

    path('image/', login_required(images.ImageList.as_view()), name='image_list'),

    path('backup/', login_required(backups.BackupList.as_view()), name='backup_list'),
]