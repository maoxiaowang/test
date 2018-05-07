# Create your tasks here
from celery import shared_task, Celery

app = Celery('storage')


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)

#
# class MyTask(Task):
#     def on_success(self, retval, task_id, args, kwargs):
#         print('task done: {0}'.format(retval))
#         return super(MyTask, self).on_success(retval, task_id, args, kwargs)
#
#     def on_failure(self, exc, task_id, args, kwargs, einfo):
#         print('task fail, reason: {0}'.format(exc))
#         return super(MyTask, self).on_failure(exc, task_id, args, kwargs, einfo)
