# Create your tasks here
import time
from celery import shared_task
from common.openstack.cinder import CinderRequest

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


def create_volumes(request, project_id, *args, **kwargs):
    """

    :param request:
    :param project_id:
    :param args:
    :param kwargs:
    :return:
    """
    #
    volume_type_data = {}
    chain = _create_volume_type.s(request, project_id, volume_type_data) | _create_volume.s(request, project_id)
    chain()


@shared_task
def _create_volume(request, project_id, *args, **kwargs):
    print('_create_volume start')
    volume_type = args[0]
    print('volume_type_id: %s' % volume_type['volume_type']['id'])
    time.sleep(15)
    print('_create_volume end')


@shared_task
def _create_volume_type(request, project_id, *args, **kwargs):
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
