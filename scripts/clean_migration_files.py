# coding=utf-8
"""

"""
import os
from ecloud.settings import BASE_DIR


GUARDIAN_DIR = r'D:\Python36\Lib\site-packages\guardian'


def clean_migrations(directories):
    assert isinstance(directories, (tuple, list))
    for item in directories:
        if os.path.exists(item):
            for root, dirs, files in os.walk(item):
                if root.endswith(r'\migrations'):
                    for f in files:
                        if f != '__init__.py':
                            os.remove(os.path.join(root, f))
                            print(os.path.join(root, f) + ' has been removed.')


if __name__ == '__main__':
    clean_migrations([BASE_DIR, GUARDIAN_DIR])
