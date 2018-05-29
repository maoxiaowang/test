# coding=utf-8
from identity.models import Resource
from cinder.models import Volumes
from nova.models import Instances


def _get_resource_detail(resource_obj):
    name = None
    if resource_obj.type == 'volume':
        obj = Volumes.objects.get(id=resource_obj.id)
    elif resource_obj.type == 'host':
        obj = None
        name = None
    elif resource_obj.type == 'instance':
        obj = Instances.objects.get(uuid=resource_obj.id)
    elif resource_obj.type == 'storage':
        obj = None
        name = None
    elif resource_obj.type == 'network':
        obj = None
        name = None
    else:
        raise ValueError
    if name is None:
        name = obj.display_name
    resource_obj.display_name = name
    return resource_obj


def resource_detail(id_or_obj):
    """
    resource detail from nova, cinder ...
    :param id_or_obj:
    :return:
    """
    if isinstance(id_or_obj, str):
        resource_obj = Resource.objects.get(id=id_or_obj)
        resource_obj = _get_resource_detail(resource_obj)

    elif isinstance(id_or_obj, Resource):
        resource_obj = _get_resource_detail(id_or_obj)
    else:
        raise ValueError
    return resource_obj
