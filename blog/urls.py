from django.urls import path
from .views import BlogListView, PostDetailView

urlpatterns = [
    path('', BlogListView.as_view(), name='blog-page'),
    path('<slug:slug>', PostDetailView.as_view(), name='post-detail')
]