from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class Settings(models.Model):
    """

    """
    item = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    type = models.CharField(max_length=255)

    class Meta:
        db_table = 'settings'
        permissions = (
            ('list_settings', _('Can see settings list')),
            ('update_settings', _('Can update settings')),
        )
