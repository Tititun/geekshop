"""geekshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from admins.views import (index,
                          admin_users,
                          admin_users_update,
                          admin_users_create,
                          admin_users_delete,
                          admin_categories,
                          admin_categories_create,
                          admin_categories_update,
                          admin_categories_delete,
                          admin_products,
                          admin_products_create,
                          admin_products_update,
                          admin_products_delete)

app_name = 'admins'
urlpatterns = [
    path('', index, name='index'),
    path('users/', admin_users, name='admin_users'),
    path('users-create/', admin_users_create, name='admin_users_create'),
    path('users-update/<int:pk>', admin_users_update, name='admin_users_update'),
    path('users-delete/<int:pk>', admin_users_delete, name='admin_users_delete'),
    path('categories/', admin_categories, name='admin_categories'),
    path('categories-create/', admin_categories_create, name='admin_categories_create'),
    path('categories-update/<int:pk>', admin_categories_update, name='admin_categories_update'),
    path('categories-delete/<int:pk>', admin_categories_delete, name='admin_categories_delete'),
    path('products/', admin_products, name='admin_products'),
    path('products-create/', admin_products_create, name='admin_products_create'),
    path('products-update/<int:pk>', admin_products_update, name='admin_products_update'),
    path('products-delete/<int:pk>', admin_products_delete, name='admin_products_delete'),

]
