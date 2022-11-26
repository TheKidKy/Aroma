from django.urls import path
from . import  views

urlpatterns = [
    path('', views.products.as_view(), name='products-page')
]