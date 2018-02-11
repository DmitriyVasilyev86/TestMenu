# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin

from .models import MenuCategories, MenuItems


class MenuCategoriesAdmin(admin.ModelAdmin):

    fields = ['name', 'verbose_name', ]
    list_display = ['__str__', ]


class MenuItemsAdmin(admin.ModelAdmin):

    fields = ['name', 'category', 'path', 'parent', ]
    list_display = ['__str__', 'category', ]


admin.site.register(MenuCategories, MenuCategoriesAdmin)
admin.site.register(MenuItems, MenuItemsAdmin)
