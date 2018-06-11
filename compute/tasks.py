# Create your tasks here
from celery import shared_task
from celery.task.base import Task


class BaseTask(Task):

    def on_failure(self, exc, task_id, args, kwargs, info):
        print('{0!r} failed: {1!r}'.format(task_id, exc))

    def on_success(self, retval, task_id, args, kwargs):
        print('{0!r} success: {1!r}'.format(task_id, retval))

    def run(self, *args, **kwargs):
        print('run')


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


if __name__ == '__main__':
    res = add.delay(5, 5)
    print(res.get())