from django.urls import path
from .views import BlogListView, PostDetailView, search, add_post_comment

urlpatterns = [
    path('', BlogListView.as_view(), name='blog-page'),
    path('', search, name='search'),
    path('<slug:slug>', PostDetailView.as_view(), name='post-detail'),
    path('add-post-comment/<int:id>', add_post_comment, name='add-post-comment'),
]