# coding=utf-8

from django.dispatch import receiver
from django.db.models.signals import post_migrate
from django.core.mail import send_mail
from django.conf.global_settings import EMAIL_HOST_USER
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission, ContentType
from common.utils.text_ import UUID


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
    subject = kwargs.get('subject', '')
    from_email = kwargs.get('from_email', EMAIL_HOST_USER)
    to = kwargs.get('to')
    content = kwargs.get('content', '')
    content_type = kwargs.get('content_type', 'text')
    assert to
    assert content_type in ('text', 'html')
    if isinstance(content, bytes):
        content = str(content, 'utf8')

    pass


def init_db_handler(sender, **kwargs):
    """initialize database at the end of migrate commands"""
    if not Permission.objects.filter(codename='list_permission').exists():
        user_model = get_user_model()
        if not user_model.objects.filter(username='admin'):
            user_model().create_superuser('admin',
                                          'admin@example.com',
                                          'password', id=UUID.uuid4)

        # add extra permissions
        group_ct_id = ContentType.objects.get(model='group').id
        perms_ct_id = ContentType.objects.get(model='permission').id
        perms = [
            (perms_ct_id, 'permission', 'list_permission', 'Can list permission'),
            (perms_ct_id, 'permission', 'detail_permission', 'Can detail permission'),
            (group_ct_id, 'group', 'list_group', 'Can list group'),
            (group_ct_id, 'group', 'detail_group', 'Can detail group'),
            (group_ct_id, 'group', 'update_group_permission', 'Can change group permission'),
        ]
        for item in perms:
            model_name, code_name, name = item[1], item[2], item[3]
            Permission.objects.get_or_create(name=name,
                                             codename=code_name,
                                             content_type_id=item[0])