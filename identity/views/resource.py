# coding=utf-8
from common.constants.resources import *
from compute.models import Instances, ComputeNodes
from identity.models import Resource
from storage.models import Volumes


def _get_resource_detail(resource_obj):
    name = None
    if resource_obj.type == VOLUME:
        obj = Volumes.objects.get(id=resource_obj.id)
    elif resource_obj.type == HOST:
        obj = None
        name = None
    elif resource_obj.type == SERVER:
        obj = Instances.objects.get(uuid=resource_obj.id)
    elif resource_obj.type == STORAGE:
        obj = None
        name = None
    elif resource_obj.type == NETWORK:
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


def get_user_resources_by_type(user, resource_type, detail=False):
    resources = Resource.objects.filter(user=user, type=resource_type)
    if resources and detail:
        if resource_type == VOLUME:
            resource_ids = [r.id for r in resources]
            resources = Volumes.objects.filter(deleted=0, id__in=resource_ids)
        elif resource_type == SERVER:
            resource_ids = [r.uuid for r in resources]
            servers = Instances.objects.filter(deleted=0)
            resources = servers.filter(deleted=0, uuid__in=resource_ids)
        elif resource_type == HOST:
            # TODO: more types
            resource_ids = [r.id for r in resources]
            hosts = ComputeNodes.objects.filter(deleted=0)
            resources = hosts.filter(deleted=0, id__in=resource_ids)
        else:
            raise ValueError
    return resources
