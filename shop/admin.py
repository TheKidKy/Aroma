from django.contrib import admin
from . import models

# Register your models here.

class productAdmin(admin.ModelAdmin):
    list_filter = ['category', 'is_active']
    list_display = ['title', 'price', 'is_active']
    list_editable = ['price', 'is_active']


admin.site.register(models.Product, productAdmin)
admin.site.register(models.ProductCategory)
admin.site.register(models.ProductBrand)
