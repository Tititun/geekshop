from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from  mainapp.models import Product, Product_Category

# Create your views here.


def index(request):
    context = {
        'title': 'главная'
    }
    return render(request, 'mainapp/index.html', context)


def products(request, id_category=0, page=1):

    if id_category:
        products = Product.objects.filter(category_id=id_category)
    else:
        products = Product.objects.all()
    print(len(products))
    paginator = Paginator(products, per_page=1)

    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)

    context = {
        'title': 'товары',
        'products': products_paginator,
        'categories': Product_Category.objects.all(),
        'category_id': id_category
    }
    return render(request, 'mainapp/products.html', context)
