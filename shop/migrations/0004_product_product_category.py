# Generated by Django 4.1.3 on 2022-11-22 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_category',
            field=models.ManyToManyField(to='shop.product_category'),
        ),
    ]
