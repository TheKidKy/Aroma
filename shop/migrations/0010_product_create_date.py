# Generated by Django 4.1.3 on 2022-12-14 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_alter_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='create_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
