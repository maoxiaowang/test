from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.backends import get_user_model

# Create your models here.

UserModel = get_user_model()


class Compute(models.Model):
    """
    云主机，测试用
    """
    id = models.CharField(max_length=36, verbose_name=_('id'), primary_key=True)
    name = models.CharField(max_length=16, verbose_name=_('username'))
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE,
                             related_name='user_of_compute')

    class Meta:
        ordering = ["name"]
        permissions = (
            ("list", _("Can see server list")),
            ("detail", _("Can see server detail")),
            ("create", _("Can create servers")),
            ("change", _("Can change servers")),
            ("delete", _("Can delete servers")),
        )
        db_table = 'compute_resource'

    def __str__(self):
        return self.name
