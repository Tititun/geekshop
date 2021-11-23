from django.shortcuts import render
from  mainapp.models import Product

# Create your views here.


def index(request):
    context = {
        'title': 'главная'
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    context = {
        'title': 'товары',
        'products': Product.objects.all()
    }
    return render(request, 'mainapp/products.html', context)
