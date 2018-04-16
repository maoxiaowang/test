# coding=utf-8
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import TemplateView
from django.urls import path
from dashboard import views


app_name = 'dashboard'

urlpatterns = [
    path('', views.index, name='index'),
]