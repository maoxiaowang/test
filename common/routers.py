"""
Router for database
"""
from ecloud.settings import INSTALLED_APPS, DATABASES

ECLOUD_APPS = [i for i in INSTALLED_APPS if not i.startswith('django.') and i != 'openstack']
DEFAULT_DB = DATABASES['default'].get('NAME', 'ecloud')


class DefaultDatabaseRouter:
    """
    A router to control all OpenStack database operations on models
    in the openstack application.
    """

    def db_for_read(self, model, **hints):
        if model._meta.app_label in ECLOUD_APPS:
            return DEFAULT_DB
        else:
            return model._meta.app_label

    def db_for_write(self, model, **hints):
        if model._meta.app_label in ECLOUD_APPS:
            return DEFAULT_DB
        else:
            return model._meta.app_label

    def allow_relation(self, obj1, obj2, **hints):
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if db == DEFAULT_DB:
            return True
        return None