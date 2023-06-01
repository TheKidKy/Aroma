# Generated by Django 4.1.3 on 2023-06-01 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0014_alter_author_level"),
    ]

    operations = [
        migrations.AlterField(
            model_name="author",
            name="level",
            field=models.CharField(
                choices=[("JR", "Junior"), ("SR", "Senior")], default="JR", max_length=2
            ),
        ),
    ]
