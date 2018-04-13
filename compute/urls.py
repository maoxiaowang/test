# coding=utf-8
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import TemplateView
from django.urls import path
from identity import views


app_name = 'compute'

urlpatterns = [
    # path('about/', login_required(TemplateView.as_view(template_name="secret.html"))),
    # path('vote/', permission_required('polls.can_vote')(views.Login.as_view())),
    path('list/', permission_required('compute.list', raise_exception=True)(views.LoginView.as_view()), name='list'),
    path('detail/', permission_required('compute.detail', raise_exception=True)(views.LoginView.as_view()), name='detail'),
]