# coding=utf-8
"""

"""
import os
from ecloud.settings import BASE_DIR


def clean_migrations():

    if os.path.exists(BASE_DIR):
        for root, dirs, files in os.walk(BASE_DIR):
            if root.endswith(r'\migrations'):
                for f in files:
                    if f != '__init__.py':
                        os.remove(os.path.join(root, f))
                        print(os.path.join(root, f) + ' has been removed.')


if __name__ == '__main__':
    print('Migration files will be permanently deleted!')
    user_input = input('Are you sure? (y/n): ')
    if user_input in ('y', 'yes'):
        clean_migrations()
    else:
        print('Canceled')

