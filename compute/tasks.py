# Create your tasks here
from celery import shared_task, Task


class BaseTask(Task):

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        print('{0!r} failed: {1!r}'.format(task_id, exc))

    def run(self, *args, **kwargs):
        pass


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)


@shared_task(
             bind=True,
             name='compute.create_server',
             rate_limit='5/m')
def create_server_task():
    pass

