# coding=utf-8
# from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import TemplateView
from django.urls import path, re_path, register_converter
from compute.views import *
from django.urls.converters import UUIDConverter

app_name = 'compute'
register_converter(UUIDConverter, 'uuid')

urlpatterns = [
    # path('about/', login_required(TemplateView.as_view(template_name="secret.html"))),
    # path('vote/', permission_required('polls.can_vote')(views.Login.as_view())),
    path('server/', server_list, name='server_list'),
    path('server/<uuid:uuid>/', server_detail, name='server_detail'),
    path('host/', host_list, name='host_list'),
    path('host/<uuid:uuid>/', host_detail, name='host_detail'),
    path('snapshot/', snap_list, name='snap_list'),
    path('image/', image_list, name='image_list'),
    path('backup/', backup_list, name='backup_list'),
]