from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, DetailView, ListView, FormView
from .models import *
from django.db.models import Q


class IndexView(TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['offer_computers'] = Product.objects.filter(category__name__contains='Computer', offer=True)
        context['computers'] = Product.objects.filter(category__name__contains='Computer')
        context['offer_laptops'] = Product.objects.filter(category__name__contains='Laptop', offer=True)
        context['laptops'] = Product.objects.filter(category__name__contains='Laptop')
        context['offer_accessories'] = Product.objects.filter(category__name__contains='Accessories', offer=True)
        context['accessories'] = Product.objects.filter(category__name__contains='Accessories')
        context['trending'] = Product.objects.filter(views__gte=100).order_by('-views')
        context['super_deals'] = Product.objects.filter(super_deals=True)
        context['banners'] = BannerImage.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        term = request.POST.get('term', '')
        searches = Product.objects.filter(
            Q(name__contains=term) | Q(category__name__contains=term) | Q(sub_category__name__contains=term))
        return render(request, 'core/search.html', {'searches': searches})


class ProductDetailView(DetailView):
    template_name = 'core/product-detail.html'
    model = Product
    context_object_name = 'item'

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        product = Product.objects.get(pk=self.kwargs.get('pk'))
        context['related'] = Product.objects.filter(category=product.category)
        return context

    def post(self, request, *args, **kwargs):
        term = request.POST.get('term', '')
        searches = Product.objects.filter(
            Q(name__contains=term) | Q(category__name__contains=term) | Q(sub_category__name__contains=term))
        return render(request, 'core/search.html', {'searches': searches})
