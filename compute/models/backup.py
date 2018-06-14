from django.db import models
from django.utils.translation import ugettext_lazy as _


class Backup(models.Model):
    """
    This model is only used for permission management
    """
    class Meta:
        managed = False
        permissions = (
            ('list_backup', _('Can see backup list')),
            ('detail_backup', _('Can see backup detail')),
            ('create_backup', _('Can create backup')),
            ('update_backup', _('Can update backup')),
            ('delete_backup', _('Can delete backup')),
        )
        default_permissions = ()
