# Create your tasks here
from celery import shared_task
from common.openstack.cinder import CinderRequest

REQUEST = CinderRequest('cinder')


@shared_task
def list_volumes(request, project_id, *args, **kwargs):
    """

    :param request: Django request object
    :param project_id:
    :param args:
    :param kwargs:
    :return:
    """

    res = REQUEST.list_volumes(request, project_id, *args, **kwargs)
    return res
