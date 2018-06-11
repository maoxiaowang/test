from celery import shared_task
from celery.task.base import Task
from django.core.mail import send_mail
from common.log import Logging
import traceback
import time

LOG = Logging.default_logger


__all__ = [
    'SendMailTask',
]


# Create your tasks here

class SendMailTask(Task):

    def on_failure(self, exc, task_id, args, kwargs, info):
        print('{0!r} failed: {1!r}'.format(task_id, exc))

    def on_success(self, retval, task_id, args, kwargs):
        print('{0!r} success: {1!r}'.format(task_id, retval))

    def run(self, *args, **kwargs):
        time.sleep(5)
        print('run')


@shared_task(name='common.send_mail')
def send_mail_task(subject, message, recipient_list, from_email=None,
                   html_message=None):
    try:
        send_mail(subject,
                  message,
                  from_email,
                  recipient_list=recipient_list,
                  html_message=html_message)
    except Exception as e:
        LOG.error('send mail by task error: %s' % e)


@shared_task
def test():
    time.sleep(5)
    print('done')


if __name__ == '__main__':
    test.delay()