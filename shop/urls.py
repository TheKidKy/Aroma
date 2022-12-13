from django.urls import path
from . import  views

urlpatterns = [
    path('', views.products.as_view(), name='products-page'),
    path('category', views.products.as_view(), name='products-by-category'),
    path('<slug:slug>', views.product_detail.as_view(), name='product-detail'),
    # path('products-by-cat', views.filter_products_by_category, name='products-by-cat')
]
