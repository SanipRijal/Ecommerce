from django.contrib import admin
from .models import *
from image_cropping.admin import ImageCroppingMixin


class ProductImage(ImageCroppingMixin, admin.TabularInline):
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


class BannerCropperAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass


admin.site.register(BannerImage, BannerCropperAdmin)