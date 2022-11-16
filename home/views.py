from django.shortcuts import render

# Create your views here.

def home_page(request):
    return render(request, 'home/index.html')

def header_references(request):
    return render(request, 'shared/references/header_references.html')

def footer_references(request):
    return render(request, 'shared/references/footer_references.html')

def header_component(request):
    return render(request, 'shared/components/header_component.html')

def footer_component(request):
    return render(request, 'shared/components/footer_component.html')