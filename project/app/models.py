from django.db import models
from django.utils.translation import gettext as _
from django.utils.translation import pgettext_lazy


class Category(models.Model):
    name = models.CharField(max_length=100, help_text=_('category name'))


class Model(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='categories',
        verbose_name=pgettext_lazy('Help text for Model', 'Help text'))
