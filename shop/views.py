from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product

# Create your views here.

class products(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'shop/products.html'

    def get_context_data(self, **kwargs):
        context = super(products, self).get_context_data()
        context['category'] = self.kwargs.get('category')
        return context
