# coding=utf-8
from django.dispatch import receiver
from django.core.signals import request_finished
from django.core.mail import EmailMultiAlternatives


def send_email_handler(sender, **kwargs):
    if kwargs.get('identifier') == 'user_created':
        pass
    print('send email')

    # subject, from_email, to = 'hello', 'from@example.com', 'to@example.com'
    # text_content = 'This is an important message.'
    # html_content = '<p>This is an <strong>important</strong> message.</p>'
    # msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    # msg.attach_alternative(html_content, "text/html")
    # msg.send()