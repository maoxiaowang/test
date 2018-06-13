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
            ('add_backup', _('Can change backup')),
            ('change_backup', _('Can change backup')),
            ('delete_backup', _('Can delete backup')),
        )
        default_permissions = ()
