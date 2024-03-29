# Generated by Django 4.1.3 on 2023-04-15 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="PostTag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(db_index=True, max_length=20)),
                (
                    "url_title",
                    models.CharField(db_index=True, max_length=20, null=True),
                ),
            ],
            options={
                "verbose_name": "Tag",
                "verbose_name_plural": "Tags",
            },
        ),
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=45)),
                ("image", models.ImageField(blank=True, null=True, upload_to="images")),
                ("description", models.TextField()),
                ("publish_date", models.DateField(auto_now_add=True)),
                ("author", models.CharField(max_length=30)),
                (
                    "is_active",
                    models.BooleanField(default=False, verbose_name="Active"),
                ),
                (
                    "tag",
                    models.ManyToManyField(to="blog.posttag", verbose_name="Post tags"),
                ),
            ],
            options={
                "verbose_name": "Post",
                "verbose_name_plural": "Posts",
            },
        ),
    ]
