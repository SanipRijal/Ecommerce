# -*- coding: utf-8 -*-

import importlib
from core.models import *
from django import template


register = template.Library()


@register.filter(name='get_related')
def get_related(product_id, counter):
    page_size = 4
    product = Product.objects.get(id=product_id)
    products = Product.objects.filter(category=product.category)[(counter-1)*page_size:(counter*page_size)]
    return products

