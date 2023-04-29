from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic import ListView

from .models import Post, PostTag

class BlogListView(ListView):
    model = Post
    template_name = 'blog/blog.html'
    context_object_name = 'posts'
    ordering = ['-publish_date']
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super(BlogListView, self).get_context_data()
        post_tags = self.kwargs.get('tag')
        context['tags'] = post_tags
        return context


class PostDetailView(DetailView):
    template_name = 'blog/post-detail.html'
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data()
        return context
