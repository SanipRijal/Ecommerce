# Generated by Django 2.2.4 on 2019-08-10 18:30

from django.db import migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20190810_1812'),
    ]

    operations = [
        migrations.AddField(
            model_name='bannerimage',
            name='cropping',
            field=image_cropping.fields.ImageRatioField('image', '1838x352', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='cropping'),
        ),
    ]