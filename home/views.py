from django.shortcuts import render

from shop.models import Product

def home_page(request):
    latest_products = Product.objects.all().order_by('-create_date')[:3]
    print(latest_products)
    return render(request, 'home/index.html', context={'latest_products': latest_products})


# ---- references and components ----
def header_references(request):
    return render(request, 'shared/references/header_references.html')

def footer_references(request):
    return render(request, 'shared/references/footer_references.html')

def header_component(request):
    return render(request, 'shared/components/header_component.html')

def footer_component(request):
    return render(request, 'shared/components/footer_component.html')

def trending_products_component(request):
    return render(request, 'home/components/trending_products_component.html')

def best_selling_component(request):
    return render(request, 'home/components/best_selling_component.html')
