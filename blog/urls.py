from django.urls import path
from .views import BlogListView, PostDetailView, search

urlpatterns = [
    path('', BlogListView.as_view(), name='blog-page'),
    path('', search, name='search'),
    path('<slug:slug>', PostDetailView.as_view(), name='post-detail')
]