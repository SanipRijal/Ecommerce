# Generated by Django 2.2.4 on 2019-08-10 18:12

from django.db import migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20190810_1644'),
    ]

    operations = [
        migrations.AddField(
            model_name='productimage',
            name='offer',
            field=image_cropping.fields.ImageRatioField('image', '380x338', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='offer'),
        ),
        migrations.AddField(
            model_name='productimage',
            name='trending_big',
            field=image_cropping.fields.ImageRatioField('image', '117x205', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='trending big'),
        ),
        migrations.AddField(
            model_name='productimage',
            name='trending_small',
            field=image_cropping.fields.ImageRatioField('image', '87x87', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='trending small'),
        ),
    ]
