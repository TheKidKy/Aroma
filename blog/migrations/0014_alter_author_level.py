# Generated by Django 4.1.3 on 2023-05-06 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0013_post_author"),
    ]

    operations = [
        migrations.AlterField(
            model_name="author",
            name="level",
            field=models.CharField(
                choices=[("Junior", "Junior"), ("Senior", "Senior")],
                default="Junior",
                max_length=10,
            ),
        ),
    ]