# coding=utf-8
from django.urls import path, register_converter
from identity.views import users, groups, permissions

from django.urls.converters import UUIDConverter, IntConverter

app_name = 'identity'

register_converter(UUIDConverter, 'uuid')
register_converter(IntConverter, 'id')
# <to_url:to_python>

urlpatterns = [
    path('user/login/', users.Login.as_view(), name='user_login'),
    path('user/logout/', users.Logout.as_view(), name='user_logout'),
    path('user/create/', users.UserCreate.as_view(), name='user_create'),
    path('user/update/<uuid:user_id>/', users.UserUpdate.as_view(), name='user_update'),
    path('user/delete/<uuid:user_id>/', users.UserDelete.as_view(), name='user_delete'),
    path('user/', users.UserList.as_view(), name='user_list'),
    path('user/detail/<uuid:user_id>/', users.UserDetail.as_view(), name='user_detail'),
    path('user/permission/update/<uuid:user_id>/', users.UserPermissionUpdate.as_view(),
         name='user_permission_update'),
    path('users/password/change/', users.PasswordChange.as_view(),
         name='users_password_change'),
    path('group/', groups.GroupList.as_view(), name='group_list'),
    path('group/create/', groups.GroupCreate.as_view(), name='group_create'),
    path('group/detail/<id:group_id>/', groups.GroupDetail.as_view(), name='group_detail'),
    path('group/update/<id:group_id>/', groups.GroupUpdate.as_view(), name='group_update'),
    path('group/delete/<id:group_id>/', groups.GroupDelete.as_view(), name='group_delete'),
    path('group/user/update/<id:group_id>/', groups.GroupUserUpdate.as_view(),
         name='group_user_update'),
    path('group/permission/update/<id:group_id>/', groups.GroupPermissionUpdate.as_view(),
         name='group_permission_update'),
    path('permission/', permissions.PermissionList.as_view(), name='permission_list'),

    # path('users/perms/update/', views.UserPermissionUpdate.as_view(),
    #      name='user_perms_update'),
    # path('group/perms/update/', views.GroupPermissionUpdate.as_view(),
    #      name='group_perms_update'),
]