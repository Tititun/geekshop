from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from mainapp.models import Product, Product_Category
from django.conf import settings
from django.core.cache import cache


def get_link_product():
    if settings.LOW_CACHE:
        key = 'link_product'
        link_product = cache.get(key)
        if link_product is None:
            link_category = Product.objects.all()
            cache.set(key, link_product)
        return link_product
    else:
        return Product.objects.all()

def get_link_category():
    if settings.LOW_CACHE:
        key = 'link_category'
        link_category = cache.get(key)
        if link_category is None:
            link_category = Product_Category.objects.all()
            cache.set(key, link_category)
        return link_category
    else:
        return Product_Category.objects.all()


def index(request):
    context = {
        'title': 'главная'
    }
    return render(request, 'mainapp/index.html', context)


def products(request, id_category=0, page=1):

    if id_category:
        # products = Product.objects.filter(category_id=id_category).select_related('category')
        products = get_link_product()
    else:
        products = Product.objects.all().select_related('category')


    paginator = Paginator(products, per_page=2)

    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)

    context = {
        'title': 'товары',
        'products': products_paginator,
        # 'categories': Product_Category.objects.all(),
        'categories': get_link_category(),
        'category_id': id_category
    }
    return render(request, 'mainapp/products.html', context)
