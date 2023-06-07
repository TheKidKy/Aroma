from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic import ListView
from django.http import HttpRequest

from utils.http_service import get_client_ip

from .models import Post, PostTag, Author, PostVisit

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
    
    def get_queryset(self):
        query = super(BlogListView, self).get_queryset()
        request: HttpRequest = self.request
        post_name = request.GET.get('search')

        if post_name is not None:
            query = query.filter(title__icontains=post_name)

        return query


class PostDetailView(DetailView):
    template_name = 'blog/post-detail.html'
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data()
        request = self.request
        loaded_post = self.object
        user_id = None
        user_ip = get_client_ip(request)

        if request.user.is_authenticated:
            user_id = request.user.id

        has_been_visited = PostVisit.objects.filter(ip__iexact=user_ip, post_id=loaded_post.id).exists()

        if not has_been_visited:
            new_visit = PostVisit(user_id=user_id, ip=user_ip, post_id=loaded_post.id)
            new_visit.save()

        context['visit_count'] = PostVisit.objects.filter(post_id=loaded_post.id).count()
        
        return context


def search(request):
    if request.method == 'GET':
        post_name = request.GET('search')
        status = Post.objects.filter(title__icontains=post_name)
        return render(request, "blog/blog.html", {"related_posts": status})
    else:
        return render(request, "blog/blog.html")