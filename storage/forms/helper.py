from django.contrib.auth import get_user_model
from ..models import Storage
from common.constants.resources import STORAGE
from django.db.utils import ProgrammingError

User = get_user_model()


def get_user_choices():
    try:
        choices = [(u.id, u.username) for u in User.objects.all()]
    except ProgrammingError:
        # auth_user table not exists
        choices = []
    return choices


def get_storage_choices(user=None):
    try:
        if user:
            storage = user.get_resources_by_type(resource_type=STORAGE,
                                                 detail=True)
        else:
            storage = Storage.objects.all()
        choices = [(s.id, s.name) for s in storage]
    except ProgrammingError:
        choices = []
    return choices
