# Create your tasks here
import time
from celery import shared_task, Task
from common.openstack.cinder import CinderRequest
from celery.worker.request import Request


R = CinderRequest()


class VolumeCreateTask(Task):

    def run(self, *args, **kwargs):
        pass

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        print('{0!r} failed: {1!r}'.format(task_id, exc))

    def on_success(self, retval, task_id, args, kwargs):
        print('{0!r} success: {1!r}'.format(task_id, retval))


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


@shared_task(base=VolumeCreateTask, bind=True)
def _create_volume(self, *args, **kwargs):
    print('_create_volume start')
    volume_type = args[0]
    print('volume_type_id: %s' % volume_type['volume_type']['id'])
    time.sleep(15)
    print('_create_volume end')
    # assign user's object permission after volume creating finished
    user_obj = None
    volume_obj = None

    # and more if it is needed


@shared_task(base=VolumeCreateTask, bind=True)
def _create_volume_type(self, *args, **kwargs):
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
