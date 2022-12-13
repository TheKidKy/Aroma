from django.shortcuts import render
from django.db.models import Count
from django.views.generic import ListView, DetailView
from .models import Product, ProductCategory, ProductBrand
from django.http import HttpResponse

# Create your views here.

class products(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'shop/products.html'

    def get_context_data(self, **kwargs):
        context = super(products, self).get_context_data()
        context['category'] = self.request.GET.get('cat')
        return context

    def get_queryset(self):
        query = super(products, self).get_queryset()
        category_name = self.request.GET.get('cat')

        if category_name is not None:
            query = query.filter(category__url_title__iexact=category_name)

        return query

class product_detail(DetailView):
    model = Product
    template_name = 'shop/product_detail.html'

def categories_component(request):
    product_categories = ProductCategory.objects.filter(is_active=True).annotate(product_count=Count('product'))
    product_brands = ProductBrand.objects.filter(is_active=True).annotate(product_count=Count('product'))
    return render(request, 'shop/components/categories.html', context={'categories': product_categories, 'brands': product_brands})

# def filter_products_by_category(request):
#     category_name = request.GET.get('category')
#     print(category_name)
#
#     return render(request, 'shop/products.html')
#     return HttpResponse('response')

