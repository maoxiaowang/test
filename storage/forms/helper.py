from django.contrib.auth import get_user_model
from ..models import Storage
from common.constants.resources import STORAGE

User = get_user_model()


def get_user_choices():
    return [(u.id, u.username) for u in User.objects.all()]


def get_storage_choices(user=None):
    if user:
        storage = user.get_resources_by_type(resource_type=STORAGE,
                                                     detail=True)
    else:
        storage = Storage.objects.all()
    return [(s.id, s.name) for s in storage ]
