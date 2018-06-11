# coding=utf-8
from django.core.mail import EmailMultiAlternatives
from django.conf.global_settings import EMAIL_HOST_USER


def send_email_handler(sender, **kwargs):
    """
    必传参数为to和content
    :param sender:
    :param kwargs:
    subject: str
    from_email: str
    to: str
    content: str
    type: str[text|html]
    :return:
    """
    # subject = kwargs.get('subject', '')
    # from_email = kwargs.get('from_email', EMAIL_HOST_USER)
    # to = kwargs.get('to')
    # content = kwargs.get('content', '')
    # content_type = kwargs.get('content_type', 'text')
    # assert to
    # assert content_type in ('text', 'html')
    # if isinstance(content, bytes):
    #     content = str(content, 'utf8')
    #
    # msg = EmailMultiAlternatives(subject, content, from_email, [to])
    # if content_type == 'html':
    #     msg.attach_alternative(content, "text/html")
    # msg.send()
    pass
