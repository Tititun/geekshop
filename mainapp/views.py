from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'title': 'главная'
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    context = {
        'title': 'товары',
        'products': [
            {
            'name': 'Стул',
            'image': 'chair_1.jpg',
            'description': 'Отличный стул',
            'price': 3050
            },
            {
                'name': 'Белый стул',
                'image': 'product-21.jpg',
                'description': 'Элитный стул',
                'price': 7250
            },
            {
                'name': 'Часы настенные',
                'image': 'product-4-sm.jpg',
                'description': 'Очень красивые',
                'price': 2100
            },
        ]
    }
    return render(request, 'mainapp/products.html', context)
