# Generated by Django 4.1.3 on 2022-12-16 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_product_create_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='create_date',
            field=models.DateField(null=True),
        ),
    ]