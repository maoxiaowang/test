# coding=utf-8
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import TemplateView
from django.urls import path
from django.conf.urls import include
from identity import views

app_name = 'identity'

urlpatterns = [
    # path('about/', login_required(TemplateView.as_view(template_name="secret.html"))),
    # path('vote/', permission_required('polls.can_vote')(VoteView.as_view())),
    path('users/login/', views.Login.as_view(), name='user_login'),
    path('users/logout/', views.Logout.as_view(), name='user_logout'),
    path('users/create/', views.UserCreate.as_view(), name='user_create'),
    path('users/update/', views.UserUpdate.as_view(), name='user_update'),
    path('users/delete/', views.UserDelete.as_view(), name='user_delete'),
    path('users/list/', views.UserList.as_view(), name='user_list'),
    path('users/detail/', views.UserDetail.as_view(), name='user_detail'),

    # path('users/perms/update/', views.UserPermissionUpdate.as_view(),
    #      name='user_perms_update'),
    # path('group/perms/update/', views.GroupPermissionUpdate.as_view(),
    #      name='group_perms_update'),

    path('users/password/change/', views.PasswordChange.as_view(),
         name='users_password_change')
]