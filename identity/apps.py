from django.apps import AppConfig
from django.db.models.signals import post_migrate


class Config(AppConfig):
    name = 'identity'

    def ready(self):
        from identity.signals import handlers
        post_migrate.connect(handlers.init_db_handler,
                             sender=self, dispatch_uid='init_db')
