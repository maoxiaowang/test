# coding=utf-8
# from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import TemplateView
from django.urls import path, re_path, register_converter
from compute.views import *
from .converters import *


app_name = 'compute'

register_converter(UUIDConverters, 'uuid')

urlpatterns = [
    # path('about/', login_required(TemplateView.as_view(template_name="secret.html"))),
    # path('vote/', permission_required('polls.can_vote')(views.Login.as_view())),
    path('server/', server_list, name='server_list'),
    path('server/<uuid:uuid>/', server_detail, name='server_detail'),

]