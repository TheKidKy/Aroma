# Generated by Django 4.1.3 on 2023-05-05 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0011_alter_post_author"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="author",
        ),
    ]