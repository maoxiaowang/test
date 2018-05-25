# coding=utf-8
from django.contrib.auth import get_user_model
from storage.models import StorageVolume
from guardian.shortcuts import get_objects_for_user, get_perms

User = get_user_model()


def get_resources(user=None, resource_type=None):
    """
    获取所有资源，可指定用户，资源类型
    :param user: User model
    :param resource_type: str/Models
    :return:
    """
    res = dict()
    # storage volume
    volumes = StorageVolume.objects.all()

    if user:
        assert isinstance(user, User)

        for item in volumes:
            obj_perms = get_perms(user, item)
            # add user's perms with certain object
            item.user_perms = obj_perms

    res['volume'] = volumes

    return res
