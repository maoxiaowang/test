from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.backends import get_user_model

# Create your models here.

UserModel = get_user_model()


# class StorageResource(models.Model):
#     """
#
#     """
#     id = models.CharField(max_length=36, verbose_name=_('id'), primary_key=True)
#     name = models.CharField(max_length=16, verbose_name=_('name'))
#     type = models.CharField(max_length=16, verbose_name=_('type'))
#
#     user = models.ForeignKey(UserModel, on_delete=models.CASCADE,
#                              related_name='storage_owner')
#
#     class Meta:
#         ordering = ['name', 'id']
#         permissions = (
#             ('storage_list', _('Can see storage list')),
#             ('storage_detail', _('Can see storage detail')),
#             ('storage_add', _('Can add storage')),
#             ('storage_change', _('Can change storage')),
#             ('storage_remove', _('Can remove storage')),
#         )
#
#     def __str__(self):
#         return self.name
#
#
class Volume(models.Model):
    """

    """
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=16, verbose_name=_('name'))
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE,
                             related_name='volume_owner')

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
