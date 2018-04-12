from django.db import models
from common.utils.validators import validate_password, validate_email

# Create your models here.


class Account(models.Model):
    """
    Region contains one or more boards
    """
    password = models.CharField(max_length=32, verbose_name='密码')
    username = models.CharField(max_length=16, verbose_name='用户名')
    email = models.EmailField(max_length=64, verbose_name='邮箱', validators=[validate_email])

    class Meta:
        ordering = ["-email"]

    def __str__(self):
        return '%s account' % self.username
