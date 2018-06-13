from django.db import models
from django.utils.translation import ugettext_lazy as _


class Storage(models.Model):
    """
    Storage modal
    """
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=255, verbose_name=_('name'))

    class Meta:
        db_table = 'storage'
        permissions = (
            ('list_storage', _('Can see storage list')),
            ('detail_storage', _('Can see storage detail')),
            ('add_storage', _('Can add storage')),
            ('change_storage', _('Can change storage')),
            ('delete_storage', _('Can delete storage')),
        )
        default_permissions = ()
