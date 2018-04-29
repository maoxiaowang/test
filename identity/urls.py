# coding=utf-8
from django.urls import path, register_converter
from identity import views

from django.urls.converters import UUIDConverter

app_name = 'identity'

register_converter(UUIDConverter, 'uuid')
# <to_url:to_python>

urlpatterns = [
    path('users/login/', views.Login.as_view(), name='user_login'),
    path('users/logout/', views.Logout.as_view(), name='user_logout'),
    path('users/create/', views.UserCreate.as_view(), name='user_create'),
    path('users/update/', views.UserUpdate.as_view(), name='user_update'),
    path('users/delete/', views.UserDelete.as_view(), name='user_delete'),
    path('users/', views.UserList.as_view(), name='user_list'),
    path('users/detail/', views.UserDetail.as_view(), name='user_detail'),
    path('group/', views.GroupList.as_view(), name='group_list'),
    path('group/detail/<uuid:uuid>', views.GroupDetail.as_view(),
         name='group_detail'),
    path('permission/', views.PermissionList.as_view(), name='permission_list'),

    # path('users/perms/update/', views.UserPermissionUpdate.as_view(),
    #      name='user_perms_update'),
    # path('group/perms/update/', views.GroupPermissionUpdate.as_view(),
    #      name='group_perms_update'),

    path('users/password/change/', views.PasswordChange.as_view(),
         name='users_password_change')
]