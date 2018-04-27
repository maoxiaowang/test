# coding=utf-8

import os
import shutil
from ecloud.settings import BASE_DIR


class ExportDB(object):

    def __init__(self, db_host, db_user, db_pass, db_name='root', db_port=3306):
        self.db_name = db_name
        self.parmas = {
            'db_host': db_host,
            'db_user': db_user,
            'db_pass': db_pass,
            'db_port': db_port,
            'db_name': db_name
        }

    def export_table_structure(self):
        os.system('ssh %(db_host)s "mysqldump --opt -d %(db_name)s '
                  '-u%(db_user)s -p%(db_pass)s > %(db_name)s.sql"' % self.parmas)
        shutil.move('%s.sql' % self.db_name,
                    os.path.join(
                        BASE_DIR, 'openstack', 'models', '%s.py' % self.db_name))
