# coding=utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Host(models.Model):
    """
    宿主机
    """
    id = models.SmallIntegerField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name=_('host name'))
    ip = models.GenericIPAddressField(verbose_name=_('IP address'))

    class Meta:
        db_table = 'host'
        permissions = (
            ('list_storage', _('Can see storage list')),
            ('detail_storage', _('Can see storage detail')),
            ('create_storage', _('Can create storage')),
            ('update_storage', _('Can update storage')),
            ('delete_storage', _('Can delete storage')),
        )
        default_permissions = ()
