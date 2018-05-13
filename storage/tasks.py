# Create your tasks here
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
