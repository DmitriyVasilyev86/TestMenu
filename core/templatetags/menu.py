# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import template
from django.http import HttpRequest
from django.urls import reverse, NoReverseMatch

from core.models import MenuItems

register = template.Library()


@register.inclusion_tag('core/menu.html', takes_context=True)
def draw_menu(context, name='', parent=0):
    """
    Draw tree menu
    :param context:
    :param name:
    :param parent:
    :return:
    """

    if parent != 0 and 'full_menu' in context:
        menu = context['full_menu']
    else:

        # Get path if request exist
        path = context['request'].path if 'request' in context and isinstance(context['request'], HttpRequest) else ''

        data = MenuItems.objects.select_related().filter(category__name=name).order_by('pk')

        menu = []

        for item in data:

            try:
                url = reverse(item.path)
            except NoReverseMatch:
                url = item.path
                target = '_blank'
            else:
                target = '_self'

            menu.append({
                'id': item.pk,
                'url': url,
                'target': target,
                'name': item.name,
                'parent': item.parent_id or 0,
                'active': True if url == path else False,
            })

    return {
        'full_menu': menu,
        'current_menu': (item for item in menu if 'parent' in item and item['parent'] == parent),
    }

