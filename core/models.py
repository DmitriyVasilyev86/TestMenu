# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class MenuCategories(models.Model):

    LABELS = {
        'name': 'Название',
        'verbose_name': 'Полное название'
    }

    class Meta:
        verbose_name = 'Категории меню'
        verbose_name_plural = 'Категории меню'

    name = models.CharField(max_length=255, verbose_name=LABELS['name'], blank=True, null=False)
    verbose_name = models.CharField(max_length=255, verbose_name=LABELS['verbose_name'], blank=True, null=False)

    def __str__(self):
        return self.verbose_name


@python_2_unicode_compatible
class MenuItems(models.Model):

    LABELS = {
        'name': 'Имя',
        'category': 'Категория',
        'path': 'Ссылка',
        'parent': 'Родительский элемент'
    }

    class Meta:
        verbose_name = 'Элементы меню'
        verbose_name_plural = 'Элементы меню'

    name = models.CharField(max_length=255, verbose_name=LABELS['name'], blank=True, null=False)

    category = models.ForeignKey(
        MenuCategories,
        verbose_name=LABELS['category'],
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )
    path = models.CharField(max_length=1000, verbose_name=LABELS['path'], blank=True, null=False)

    parent = models.ForeignKey(
        'self',
        verbose_name=LABELS['parent'],
        on_delete=models.SET_DEFAULT,
        null=True,
        blank=True,
        default=0
    )

    def __str__(self):
        return self.name
