# coding=utf-8
"""
Models for OpenStack databases
"""
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Volumes(models.Model):
    """

    """
    created_at = models.DateTimeField(verbose_name=_('created_at'), default=None)
    updated_at = models.DateTimeField(verbose_name=_('updated_at'), default=None)
    deleted_at = models.DateTimeField(verbose_name=_('deleted_at'), default=None)
    deleted = models.SmallIntegerField(max_length=1, default=None)
    id = models.CharField(max_length=36)
    ec2_id = models.CharField(max_length=255, default=None)


    class Meta:
        db_table = 'nova'
        ordering = ['name', 'id']

    def __str__(self):
        return self.name

