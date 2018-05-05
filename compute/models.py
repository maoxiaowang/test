# coding=utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.backends import get_user_model

# Create your models here.

# UserModel = get_user_model()


# class Server(models.Model):
#     """
#     云主机
#     """
#     id = models.CharField(max_length=36, verbose_name=_('id'), primary_key=True)
#     name = models.CharField(max_length=16, verbose_name=_('name'))
#     # 虚拟机所属用户
#     user = models.ForeignKey(UserModel, on_delete=models.CASCADE,
#                              related_name='server_owner')
#
#     class Meta:
#         db_table = 'compute_server'
#         ordering = ['name', 'id']
#         permissions = (
#             ('list_server', _('Can see server list')),
#             ('detail_server', _('Can see server detail')),
#             ('create_server', _('Can create server')),
#             ('change_server', _('Can change server')),
#             ('delete_server', _('Can delete server')),
#         )
#         default_permissions = ()
#
#     def __str__(self):
#         return self.name
#
#
class Host(models.Model):
    """
    宿主机
    """
    id = models.CharField(max_length=36, verbose_name=_('id'), primary_key=True)
    name = models.CharField(max_length=16, verbose_name=_('username'), blank=True)

    class Meta:
        db_table = 'compute_host'
        ordering = ['name', 'id']
        permissions = (
            ('list_host', _('Can see host list')),
            ('detail_host', _('Can see host detail')),
            ('add_host', _('Can add host')),
            ('change_host', _('Can change host')),
            ('remove_host', _('Can remove host')),
        )
        default_permissions = ()

    def __str__(self):
        return self.name
#
#
# class Snapshot(models.Model):
#     id = models.CharField(max_length=36, verbose_name=_('id'), primary_key=True)
#     name = models.CharField(max_length=16, verbose_name=_('username'), blank=True)
#     user = models.ForeignKey(UserModel, on_delete=models.CASCADE,
#                              related_name='snapshot_owner')
#
#     class Meta:
#         db_table = 'compute_snapshot'
#         ordering = ['name', 'id']
#         permissions = (
#             ('list_snapshot', _('Can see snapshot list')),
#             ('detail_snapshot', _('Can see snapshot detail')),
#             ('create_snapshot', _('Can create snapshot')),
#             ('change_snapshot', _('Can change snapshot')),
#             ('delete_snapshot', _('Can delete snapshot')),
#         )
#         default_permissions = ()
#
#     def __str__(self):
#         return self.name
#
#
# class Image(models.Model):
#     id = models.CharField(max_length=36, verbose_name=_('id'), primary_key=True)
#     name = models.CharField(max_length=16, verbose_name=_('username'), blank=True)
#     user = models.ForeignKey(UserModel, on_delete=models.CASCADE,
#                              related_name='image_owner')
#
#     class Meta:
#         db_table = 'compute_image'
#         ordering = ['name', 'id']
#         permissions = (
#             ('list_image', _('Can see image list')),
#             ('detail_image', _('Can see image detail')),
#             ('upload_image', _('Can upload image')),
#             ('download_image', _('Can download image')),
#             ('change_image', _('Can change image')),
#             ('delete_image', _('Can delete image')),
#         )
#         default_permissions = ()
#
#     def __str__(self):
#         return self.name
#
#
# class Backup(models.Model):
#     id = models.CharField(max_length=36, verbose_name=_('id'), primary_key=True)
#     name = models.CharField(max_length=16, verbose_name=_('username'), blank=True)
#     user = models.ForeignKey(UserModel, on_delete=models.CASCADE,
#                              related_name='backup_owner')
#
#     class Meta:
#         db_table = 'compute_backup'
#         ordering = ['name', 'id']
#         permissions = (
#             ('list_backup', _('Can see backup list')),
#             ('detail_backup', _('Can see backup detail')),
#             ('create_backup', _('Can create backup')),
#             ('change_backup', _('Can change backup')),
#             ('delete_backup', _('Can delete backup')),
#         )
#         default_permissions = ()
#
#     def __str__(self):
#         return self.name
