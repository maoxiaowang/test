from django.db import models

# Create your models here.


# class Menu(models.Model):
#     """
#     Menu contains one or more sub menu
#     """
#     name = models.CharField(max_length=16, verbose_name='menu_identifier',
#                             unique=True)
#     display_name = models.CharField(max_length=32, verbose_name='display_name')
#
#     def __str__(self):
#         return self.display_name
#
#     class Meta:
#         db_table = 'dashboard_menu'
#
#
# class SubMenu(models.Model):
#     """
#     Submenu
#     """
#     name = models.CharField(max_length=16, verbose_name='submenu_identifier',
#                             unique=True)
#     display_name = models.CharField(max_length=32, verbose_name='display_name')
#     menu = models.ForeignKey(to=Menu, on_delete=models.CASCADE,
#                              related_name='menu_of_submenu')
#
#     def __str__(self):
#         return self.display_name
#
#     class Meta:
#         db_table = 'dashboard_sub_menu'
