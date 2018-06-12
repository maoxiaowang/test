from django.db import models
from django.utils.translation import ugettext_lazy as _


class Snapshot(models.Model):
    """
    This model is only used for permission management
    """
    class Meta:
        managed = False
        permissions = (
            ('list_snapshot', _('Can see snapshot list')),
            ('detail_snapshot', _('Can see snapshot detail')),
            ('create_snapshot', _('Can create snapshot')),
            ('update_snapshot', _('Can update snapshot')),
            ('delete_snapshot', _('Can delete snapshot')),
        )
        default_permissions = ()
