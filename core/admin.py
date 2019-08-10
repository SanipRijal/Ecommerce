from django.contrib import admin
from .models import *


class ProductImage(admin.TabularInline):
    model = ProductImage


class ProductHighlight(admin.TabularInline):
    model = ProductHighlight


class ProductSpecificationType(admin.TabularInline):
    model = ProductSpecificationType


class ProductSpecification(admin.TabularInline):
    model = ProductSpecification


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductHighlight, ProductImage, ProductSpecificationType, ProductSpecification]


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(BannerImage)