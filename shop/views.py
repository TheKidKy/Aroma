from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product, ProductCategory, ProductBrand
from django.db.models import Count

# Create your views here.

class products(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'shop/products.html'
    ordering = ['-create_date']

    def get_context_data(self, **kwargs):
        context = super(products, self).get_context_data()
        return context

class product_detail(DetailView):
    model = Product
    template_name = 'shop/product_detail.html'

    def get_context_data(self, **kwargs):
        context = super(product_detail, self).get_context_data(**kwargs)
        return context

def categories_component(request):
    product_categories = ProductCategory.objects.filter(is_active=True).annotate(product_count=Count('product'))
    product_brands = ProductBrand.objects.filter(is_active=True).annotate(product_count=Count('product'))
    return render(request, 'shop/components/categories.html', context={'categories': product_categories, 'brands': product_brands})

