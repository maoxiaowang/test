# coding=utf-8
from django.urls import path, register_converter
from identity.views import user, group, permission

from django.urls.converters import UUIDConverter, IntConverter

app_name = 'identity'

register_converter(UUIDConverter, 'uuid')
register_converter(IntConverter, 'id')
# <to_url:to_python>

urlpatterns = [
    path('user/login/', user.Login.as_view(), name='user_login'),
    path('user/logout/', user.Logout.as_view(), name='user_logout'),
    path('user/create/', user.UserCreate.as_view(), name='user_create'),
    path('user/update/<uuid:user_id>/', user.UserUpdate.as_view(), name='user_update'),
    path('user/delete/<uuid:user_id>/', user.UserDelete.as_view(), name='user_delete'),
    path('user/', user.UserList.as_view(), name='user_list'),
    path('user/detail/<uuid:user_id>/', user.UserDetail.as_view(), name='user_detail'),
    path('user/permission/update/<uuid:user_id>/', user.UserPermissionUpdate.as_view(),
         name='user_permission_update'),
    path('users/password/change/', user.PasswordChange.as_view(),
         name='users_password_change'),
    path('group/', group.GroupList.as_view(), name='group_list'),
    path('group/create/', group.GroupCreate.as_view(), name='group_create'),
    path('group/detail/<id:group_id>/', group.GroupDetail.as_view(), name='group_detail'),
    path('group/update/<id:group_id>/', group.GroupUpdate.as_view(), name='group_update'),
    path('group/delete/<id:group_id>/', group.GroupDelete.as_view(), name='group_delete'),
    path('group/user/update/<id:group_id>/', group.GroupUserUpdate.as_view(),
         name='group_user_update'),
    path('group/permission/update/<id:group_id>/', group.GroupPermissionUpdate.as_view(),
         name='group_permission_update'),
    path('permission/', permission.PermissionList.as_view(), name='permission_list'),

    # path('users/perms/update/', views.UserPermissionUpdate.as_view(),
    #      name='user_perms_update'),
    # path('group/perms/update/', views.GroupPermissionUpdate.as_view(),
    #      name='group_perms_update'),
]