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
            ('list_settings', _('Can see settings list')),
            ('change_settings', _('Can change settings')),
        )
