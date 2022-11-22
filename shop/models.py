from django.db import models

class product(models.Model):
    COLOR_CHOICES = (
        ('B', 'Black'),
        ('Y', 'Yellow'),
    )
    title = models.CharField(max_length=25)
    # todo: adding product category with a many-to-many rel
    # todo: adding product brand with a one-to-many rel
    color = models.CharField(max_length=10, choices=COLOR_CHOICES)
    image = models.ImageField(null=True)
    price = models.IntegerField()
    description = models.TextField(db_index=True)
    slug = models.SlugField(default="", null=False, db_index=True, blank=True, max_length=200, unique=True,
                            verbose_name='slug title')
    is_active = models.BooleanField(default=False, verbose_name='active')



