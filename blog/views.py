from typing import Any
from django.db.models.query import QuerySet
from django.db.models import Count
from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic import ListView
from django.http import HttpRequest, HttpResponseRedirect

from utils.http_service import get_client_ip

from .models import Post, PostTag, Author, PostVisit, PostComment
from .forms import PostCommentForm


class BlogListView(ListView):
    model = Post
    template_name = 'blog/blog.html'
    context_object_name = 'posts'
    queryset = Post.objects.annotate(views=Count('postvisit')).filter(is_active=True)
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

        post: Post = kwargs.get('object')

        context['visit_count'] = PostVisit.objects.filter(post_id=loaded_post.id).count()
        context['comment_form'] = PostCommentForm()
        context['comments'] = PostComment.objects.filter(post_id=post.id, parent=None).order_by('-create_date').prefetch_related('postcomment_set')
        context['comments_count'] = PostComment.objects.filter(post_id=post.id).count()

        return context


def search(request):
    if request.method == 'GET':
        post_name = request.GET('search')
        status = Post.objects.filter(title__icontains=post_name)
        return render(request, "blog/blog.html", {"related_posts": status})
    else:
        return render(request, "blog/blog.html")
    

def add_post_comment(request: HttpRequest, id):
    if request.method == 'POST':
        comment_form = PostCommentForm(request.POST)
        if comment_form.is_valid():
            content = comment_form.cleaned_data.get('content')
            subject = comment_form.cleaned_data.get('subject')
            email = comment_form.cleaned_data.get('email')
            name = comment_form.cleaned_data.get('name')
            new_comment = PostComment(content=content, subject=subject, email=email, name=name, post_id=id)
            new_comment.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))