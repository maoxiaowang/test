"""
Router for database
"""

DEFAULT_DB_ALIAS = 'default'
OPENSTACK_DB_ALIAS = ['cinder', 'glance', 'keystone', 'neutron', 'nova']


class DefaultDatabaseRouter:
    """
    A router to control all OpenStack database operations on models
    in the openstack application.
    """

    def db_for_read(self, model, **hints):
        if model._meta.app_label in OPENSTACK_DB_ALIAS:
            return model._meta.app_label
        else:
            return DEFAULT_DB_ALIAS

    def db_for_write(self, model, **hints):
        if model._meta.app_label in OPENSTACK_DB_ALIAS:
            return model._meta.app_label
        else:
            return DEFAULT_DB_ALIAS

    def allow_relation(self, obj1, obj2, **hints):
        if (obj1._state.db in [DEFAULT_DB_ALIAS] and
                obj2._state.db in [DEFAULT_DB_ALIAS]):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        # if db == DEFAULT_DB:
        #     return True
        # return None
        return True
