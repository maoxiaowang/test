from django.db import models
from django.utils.translation import ugettext_lazy as _


class Volume(models.Model):
    """
    This model is only used for permission management
    """
    class Meta:
        managed = False
        permissions = (
            ('list_volume', _('Can see volume list')),
            ('detail_volume', _('Can see volume detail')),
            ('add_volume', _('Can add volume')),
            ('change_volume', _('Can change volume')),
            ('delete_volume', _('Can delete volume')),
        )
        default_permissions = ()
