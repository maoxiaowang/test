from django.contrib.contenttypes.models import ContentType
from django.db.models import Q
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from guardian.models import UserObjectPermission, GroupObjectPermission
from identity.models import User


@receiver(pre_delete, sender=User, dispatch_uid='remove_perm_objs_with_user')
def remove_perm_objs_with_user(sender, instance, **kwargs):
    """
    Remove guardian perms when deleting a user using signal
    Or consider to override delete method in User model
    :param sender:
    :param instance:
    :param kwargs:
    :return:
    """
    filters = Q(content_type=ContentType.objects.get_for_model(instance),
                object_pk=instance.pk)
    UserObjectPermission.objects.filter(filters).delete()
    GroupObjectPermission.objects.filter(filters).delete()
