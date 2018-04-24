# coding=utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.backends import get_user_model

# Create your models here.

UserModel = get_user_model()


class Server(models.Model):
    """
    云主机
    """
    id = models.CharField(max_length=36, verbose_name=_('id'), primary_key=True)
    name = models.CharField(max_length=16, verbose_name=_('username'))
    # 虚拟机所属用户
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE,
                             related_name='user_of_server')

    class Meta:
        ordering = ['name', 'id']
        permissions = (
            ('server_list', _('Can see server list')),
            ('server_detail', _('Can see server detail')),
            ('server_create', _('Can create server')),
            ('server_change', _('Can change server')),
            ('server_delete', _('Can delete server')),
        )

    def __str__(self):
        return self.name


class Host(models.Model):
    """
    宿主机
    """
    id = models.CharField(max_length=36, verbose_name=_('id'), primary_key=True)
    name = models.CharField(max_length=16, verbose_name=_('username'), blank=True)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE,
                             related_name='user_of_host')

    class Meta:
        ordering = ['name', 'id']
        permissions = (
            ('host_list', _('Can see host list')),
            ('host_detail', _('Can see host detail')),
            ('host_add', _('Can add host')),
            ('host_change', _('Can change host')),
            ('host_remove', _('Can remove host')),
        )

    def __str__(self):
        return self.name
