from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic import ListView

from .models import Post

class BlogListView(ListView):
    model = Post
    template_name = 'blog/blog.html'
    context_object_name = 'posts'
    ordering = ['-publish_date']

    def get_context_data(self, **kwargs):
        context = super(BlogListView, self).get_context_data()
        return context

