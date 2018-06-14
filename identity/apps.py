from django.apps import AppConfig


class Config(AppConfig):
    name = 'identity'

    def ready(self):
        pass
