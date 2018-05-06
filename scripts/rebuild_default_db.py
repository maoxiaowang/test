# coding=utf-8
"""
Rebuild database
"""
from MySQLdb import connect
from ecloud.settings import DATABASES
from .clean_migration_files import clean_migrations


def get_conn():
    db = DATABASES['default']
    return connect(host=db['HOST'],
                   user=db['USER'],
                   password=db['PASSWORD'],
                   db=db['NAME'],
                   port=db['PORT'])


def drop_db():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute('DROP ecloud')
    cur.close()
    conn.close()


def rebuild_db():
    pass


if __name__ == '__main__':
    drop_db()
    clean_migrations()