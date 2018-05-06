# coding=utf-8

import os
from ecloud.settings import BASE_DIR, DATABASES


if __name__ == '__main__':
    for db in DATABASES:
        # cinder, nova, neutron ...
        db_name = DATABASES[db]['NAME']
        os.system('python3 manage.py inspectdb --database %s > %s' %
                  (db_name, os.path.join(BASE_DIR, db_name, 'models.py')))
