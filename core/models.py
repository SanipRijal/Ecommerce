from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='sub_categories')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.category.name + '-' + self.name


class Product(models.Model):
    name = models.TextField()
    previous_price = models.CharField(max_length=100, help_text=('e.g., Rs. 150000'), null=True, blank=True)
    new_price = models.CharField(max_length=100, help_text=('e.g., Rs. 150000'), null=True, blank=True)
    category = models.ForeignKey(Category, verbose_name='Category', on_delete=models.CASCADE, related_name='product_category')
    sub_category = models.ForeignKey(SubCategory, verbose_name='Sub-Category', on_delete=models.CASCADE, related_name='product_sub_category')
    views = models.IntegerField(default=0)
    super_deals = models.BooleanField(default=False, verbose_name='Do you want this item to display in super deals section?')
    offer = models.BooleanField(default=False, verbose_name='Does this item have an offer?')

    def __str__(self):
        return self.name


class ProductHighlight(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='highlights')
    highlight = models.TextField(help_text='Enter the highlight text here')


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products/')


class ProductSpecificationType(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='specification_type')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ProductSpecification(models.Model):
    type = models.ForeignKey(ProductSpecificationType, on_delete=models.CASCADE, related_name='specifications')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='specifications')
    specification_title = models.CharField(max_length=100)
    specification_value = models.CharField(max_length=100)


class BannerImage(models.Model):
    image = models.ImageField(upload_to='banners/')


