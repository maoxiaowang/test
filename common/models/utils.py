from django.apps import apps as django_apps


def get_storage_model():
    return django_apps.get_model('storage.Storage', require_ready=False)


def get_nova_instance_model():
    return django_apps.get_model('compute.Instances', require_ready=False)


def get_cinder_volume_model():
    return django_apps.get_model('storage.Volumes', require_ready=False)


def get_resource_model():
    return django_apps.get_model('identity.Resource', require_ready=False)