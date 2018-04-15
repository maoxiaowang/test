from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class ComputeModel(models.Model):
    """
    云主机，测试用
    """
    id = models.CharField(max_length=36, verbose_name=_('id'), primary_key=True)
    name = models.CharField(max_length=16, verbose_name=_('username'))

    class Meta:
        ordering = ["-name"]
        permissions = (
            ("list", _("Can see instance list")),
            ("detail", _("Can see instance detail")),
            ("create", _("Can create an instance")),
            ("delete", _("Can delete an instance")),
        )

    def __str__(self):
        return self.name
