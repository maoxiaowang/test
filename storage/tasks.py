# Create your tasks here
import time
from celery import shared_task
from common.openstack.cinder import CinderRequest
from guardian.shortcuts import assign_perm


R = CinderRequest()


@shared_task
def list_volumes(request, project_id, *args, **kwargs):
    """

    :param request: Django request object
    :param project_id:
    :param args:
    :param kwargs:
    :return:
    """

    res = R.list_volumes(request, project_id, *args, **kwargs)
    return res


def create_volumes(request, **kwargs):
    """

    :param request:
    :param kwargs:
    :return:
    """
    #
    data = request.POST
    volume_type_data = {}
    chain = _create_volume_type.s(request, volume_type_data) | _create_volume.s(request)
    chain()


@shared_task
def _create_volume(request, *args, **kwargs):
    print('_create_volume start')
    volume_type = args[0]
    print('volume_type_id: %s' % volume_type['volume_type']['id'])
    time.sleep(15)
    print('_create_volume end')
    # assign user's object permission after volume creating finished
    user_obj = None
    volume_obj = None

    assign_perm('update_volume', user_obj, obj=volume_obj)
    assign_perm('delete_volume', user_obj, obj=volume_obj)
    # and more if it is needed


@shared_task
def _create_volume_type(request, *args, **kwargs):
    """

    :param request:
    :param project_id:
    :param args:
    :param kwargs:
    :return:
    """
    print('_create_volume_type start')
    time.sleep(5)
    result = {
        "volume_type": {
            "name": "test_type",
            "extra_specs": {},
            "os-volume-type-access:is_public": True,
            "is_public": True,
            "id": "6d0ff92a-0007-4780-9ece-acfe5876966a",
            "description": "test_type_desc"
        }
    }
    print('_create_volume_type end')
    return result
