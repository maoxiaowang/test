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
            ('list', _('Can see server list')),
            ('detail', _('Can see server detail')),
            ('create', _('Can create server')),
            ('change', _('Can change server')),
            ('delete', _('Can delete server')),
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
            ('list', _('Can see host list')),
            ('detail', _('Can see host detail')),
            ('add', _('Can add host')),
            ('change', _('Can change host')),
            ('remove', _('Can remove host')),
        )

    def __str__(self):
        return self.name
