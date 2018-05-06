# coding=utf-8
from django import template

register = template.Library()


@register.filter(expects_localtime=True, is_safe=True)
def check_perms(perm_obj):
    pass
