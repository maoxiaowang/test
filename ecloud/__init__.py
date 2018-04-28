# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
from .celery import app as celery_app
from django.contrib.auth import get_user_model

__all__ = ['celery_app']

# Initialize admin user if it does not been created,
# And give all permissions to admin.
# TODO:

def init_admin_account():
    model = get_user_model()
    if not model.objects.filter(username='admin'):
        model().create_user('admin',
                            email='admin@example.com',
                            password='password',
                            )


if __name__ == '__main__':
    init_admin_account()