from django.db import models
from django.utils.translation import ugettext_lazy as _


class Server(models.Model):
    """
    This model is only used for permission management
    """
    class Meta:
        managed = False
        permissions = (
            ('list_server', _('Can see server list')),
            ('detail_server', _('Can see server detail')),
            ('create_server', _('Can create server')),
            ('update_server', _('Can update server')),
            ('delete_server', _('Can delete server')),
        )
        default_permissions = ()
