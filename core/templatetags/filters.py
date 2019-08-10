# -*- coding: utf-8 -*-

import importlib
from core.models import *
from django import template


register = template.Library()


@register.filter(name='get_related')
def get_related(product_id):
    product = Product.objects.get(id=product_id)
    return Product.objects.filter(category=product.category)[:4]

