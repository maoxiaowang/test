from django.db import models
from django.utils.translation import ugettext_lazy as _


class Image(models.Model):
    """
    This model is only used for permission management
    """
    class Meta:
        managed = False
        permissions = (
            ('list_image', _('Can see image list')),
            ('detail_image', _('Can see image detail')),
            ('create_image', _('Can create image')),
            ('update_image', _('Can update image')),
            ('delete_image', _('Can delete image')),
        )
        default_permissions = ()
