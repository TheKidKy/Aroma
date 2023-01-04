from django.shortcuts import render
from django.db.models import Count
from django.views.generic import ListView, DetailView
from django.http import HttpResponseRedirect
from utils.convertors import group_list

from .models import Product, ProductCategory, ProductBrand, ProductComment
from .forms import CommentForm


# Create your views here.

class products(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'shop/products.html'
    ordering = ['-create_date']

    def get_context_data(self, **kwargs):
        context = super(products, self).get_context_data()
        return context


class product_detail(DetailView):
    model = Product
    template_name = 'shop/product_detail.html'

    def get_context_data(self, **kwargs):
        context = super(product_detail, self).get_context_data(**kwargs)
        current_product = self.object

        context['related_products'] = group_list(
            list(Product.objects.filter(brand_id=current_product.brand_id).exclude(pk=current_product.id).all()[:12]), 3)
        context['comment_form'] = CommentForm

        return context


def add_comment(request, id):
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            msg = comment_form.cleaned_data.get('message')
            user = comment_form.cleaned_data.get('user_name')
            email = comment_form.cleaned_data.get('email')
            new_comment = ProductComment(message=msg, user_name=user, email=email, product_id=id)
            new_comment.save()

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def categories_component(request):
    product_categories = ProductCategory.objects.filter(is_active=True).annotate(product_count=Count('product'))
    product_brands = ProductBrand.objects.filter(is_active=True).annotate(product_count=Count('product'))
    return render(request, 'shop/components/categories.html',
                  context={'categories': product_categories, 'brands': product_brands})


def comments_component(request, id):
    product_id = id
    comments = ProductComment.objects.filter(product_id=product_id)
    return render(request, 'shop/components/comments_component.html', context={'comments': comments})
