from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.views.decorators.cache import cache_page, never_cache

from mainapp.models import Product, Product_Category
from django.conf import settings
from django.core.cache import cache


def get_link_product(pk='all'):
    if settings.LOW_CACHE:
        key = f'link_product_{pk}'
        link_product = cache.get(key)
        if link_product is None:
            if pk == 'all':
                link_product = Product.objects.all()
            else:
                link_product = Product.objects.filter(pk=pk)
            cache.set(key, link_product)
        return link_product
    else:
        return Product.objects.all()

def get_link_category(pk='all'):
    if settings.LOW_CACHE:
        key = f'link_category_{pk}'
        link_category = cache.get(key)
        if link_category is None:
            if pk == 'all':
                link_category = Product_Category.objects.all()
            else:
                link_category = Product_Category.objects.filter(pk=pk)
            cache.set(key, link_category)
        return link_category
    else:
        return Product_Category.objects.all()


def index(request):
    context = {
        'title': 'главная'
    }
    return render(request, 'mainapp/index.html', context)

# @cache_page(3600)
# @never_cache
def products(request, id_category=0, page=1):

    if id_category:
        # products = Product.objects.filter(category_id=id_category).select_related('category')
        products = get_link_product(pk=id_category)
    else:
        products = get_link_product(pk=id_category)
        # products = Product.objects.all().select_related('category')

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
