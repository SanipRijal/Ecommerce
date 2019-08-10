from .models import *


def header_processor(request):
    categories = Category.objects.all().order_by('name')
    return {'categories': categories}
