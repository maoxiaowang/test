# coding=utf8
from django.contrib.auth import get_user_model
UserModel = get_user_model()


class AccountAuthBackend(object):

    @staticmethod
    def authenticate(username=None, password=None):
        try:
            user = UserModel.objects.get(username=username)
            if user.check_password(password):
                return user
        except UserModel.DoesNotExist:
            return None

    @staticmethod
    def get_user(id_):
        try:
            return UserModel.objects.get(pk=id_)  # <-- tried to get by email here
        except UserModel.DoesNotExist:
            return None