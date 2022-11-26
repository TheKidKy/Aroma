from django.db import models

class ProductCategory(models.Model):
    title = models.CharField(max_length=20, db_index=True)
    url_title = models.CharField(max_length=20, db_index=True, verbose_name='url title')
    is_active = models.BooleanField(verbose_name='active')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class ProductBrand(models.Model):
    title = models.CharField(max_length=20)
    url_title = models.CharField(max_length=20, verbose_name='url title')
    is_active = models.BooleanField(verbose_name='active')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'brand'
        verbose_name_plural = 'brands'

class Product(models.Model):
    COLOR_CHOICES = (
        ('B', 'Black'),
        ('Y', 'Yellow'),
    )
    title = models.CharField(max_length=25)
    brand = models.ForeignKey(ProductBrand, on_delete=models.CASCADE, null=True, blank=True)
    color = models.CharField(max_length=10, choices=COLOR_CHOICES)
    image = models.ImageField(null=True)
    price = models.IntegerField()
    description = models.TextField(db_index=True)
    slug = models.SlugField(default="", null=False, db_index=True, blank=True, max_length=200, unique=True,
                            verbose_name='slug title')
    category = models.ManyToManyField(ProductCategory)
    is_active = models.BooleanField(default=False, verbose_name='active')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'





