from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from mainapp.models import Product, Product_Category
from django.conf import settings
from django.core.cache import cache
from django.db.models import Q, Count


def get_link_product(pk=False):
    filter = Q(category_id=pk) if pk else Q()
    if settings.LOW_CACHE:
        key = f'link_product_{pk}'
        sentinel = object()
        link_product = cache.get(key, sentinel)
        if link_product is sentinel:
            link_product = Product.objects.filter(filter)\
                .select_related('category')
            cache.set(key, link_product)
        return link_product
    else:
        return Product.objects.filter(filter).select_related('category')

def get_link_category(pk=False):
    filter = Q(pk=pk) if pk else Q()
    if settings.LOW_CACHE:
        key = f'link_category_{pk}'
        sentinel = object()
        link_category = cache.get(key, sentinel)
        if link_category is sentinel:
            link_category = Product_Category.objects.filter(filter)
            cache.set(key, link_category)
        return link_category
    else:
        return Product_Category.objects.filter(filter)\
            .annotate(total=Count('product')).exclude(total=0)


def index(request):
    context = {
        'title': 'главная'
    }
    return render(request, 'mainapp/index.html', context)

def products(request, id_category=0, page=1):

    if id_category:
        products = get_link_product(pk=id_category)
    else:
        products = get_link_product()

    paginator = Paginator(products, per_page=3)

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
