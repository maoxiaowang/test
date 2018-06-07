from django.db import models
from django.utils.translation import ugettext_lazy as _


class Storage(models.Model):
    """

    """
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=255, verbose_name=_('name'))

    class Meta:
        db_table = 'storage'
        permissions = (
            ('list_volume', _('Can see volume list')),
            ('detail_volume', _('Can see volume detail')),
            ('create_volume', _('Can create volume')),
            ('update_volume', _('Can update volume')),
            ('delete_volume', _('Can delete volume')),
        )
        default_permissions = ()