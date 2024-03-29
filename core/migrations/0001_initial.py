# Generated by Django 2.2.4 on 2019-08-03 09:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='core.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('previous_price', models.CharField(blank=True, help_text='e.g., Rs. 150000', max_length=100, null=True)),
                ('new_price', models.CharField(blank=True, help_text='e.g., Rs. 150000', max_length=100, null=True)),
                ('views', models.IntegerField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_category', to='core.Category', verbose_name='Category')),
                ('sub_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_sub_category', to='core.Category', verbose_name='Sub-Category')),
            ],
        ),
        migrations.CreateModel(
            name='ProductSpecificationType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='specification_type', to='core.Product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductSpecification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specification_title', models.CharField(max_length=100)),
                ('specification_value', models.CharField(max_length=100)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='specifications', to='core.Product')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='specifications', to='core.ProductSpecificationType')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='products/')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='core.Product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductHighlight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('highlight', models.TextField(help_text='Enter the highlight text here')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='highlights', to='core.Product')),
            ],
        ),
    ]
