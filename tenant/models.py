from django.db import models
from django.contrib.auth.backends import get_user_model

# Create your models here.


class TenantModel(models.Model):
    """
    Menu contains one or more sub menu
    """
    id = models.CharField(max_length=64, verbose_name='id', primary_key=True)
    name = models.CharField(max_length=64, verbose_name='menu_identifier',
                            primary_key=True)
    user = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE,
                             related_name='user_of_tenant')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tenants'
