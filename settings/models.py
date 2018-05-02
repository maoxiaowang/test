from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class GlobalSettings(models.Model):
    """

    """
    item = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    type = models.CharField(max_length=255)

    class Meta:
        db_table = 'settings'
        permissions = (
            ('settings_list', _('Can see settings list')),
            ('settings_create', _('Can create settings')),
            ('settings_update', _('Can update settings')),
            ('settings_delete', _('Can delete settings')),
        )
