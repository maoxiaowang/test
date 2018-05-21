from django.db import models
from django.utils.translation import ugettext_lazy as _
# from django.contrib.auth.backends import get_user_model
#
# UserModel = get_user_model()


class VolumeResource(models.Model):
    """

    """
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=16, verbose_name=_('name'))
    # user = models.ForeignKey(UserModel, on_delete=models.CASCADE,
    #                          related_name='volume_owner')

    class Meta:
        db_table = 'storage_volume'
        permissions = (
            ('list_volume', _('Can see volume list')),
            ('detail_volume', _('Can see volume detail')),
            ('create_volume', _('Can create volume')),
            ('update_volume', _('Can update volume')),
            ('delete_volume', _('Can delete volume')),
        )
        default_permissions = ()
