from django.urls import path
from . import  views

urlpatterns = [
    path('', views.products.as_view(), name='products-page'),
    path('', views.search, name='search-products'),
    path('<slug:slug>', views.product_detail.as_view(), name='product-detail'),
    path('add-post-comment/<int:id>', views.add_comment, name='product-add-comment')
]