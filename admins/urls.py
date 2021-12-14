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
                          UserListView,
                          UserUpdateView,
                          UserCreateView,
                          UserDeleteView,
                          CategoryListView,
                          CategoryCreateView,
                          CategoryUpdateView,
                          CategoryDeleteView,
                          ProductListView,
                          ProductCreateView,
                          ProductUpdateView,
                          ProductDeleteView)

app_name = 'admins'
urlpatterns = [
    path('', index, name='index'),
    path('users/', UserListView.as_view(), name='admin_users'),
    path('users-create/', UserCreateView.as_view(), name='admin_users_create'),
    path('users-update/<int:pk>', UserUpdateView.as_view(), name='admin_users_update'),
    path('users-delete/<int:pk>', UserDeleteView.as_view(), name='admin_users_delete'),
    path('categories/', CategoryListView.as_view(), name='admin_categories'),
    path('categories-create/', CategoryCreateView.as_view(), name='admin_categories_create'),
    path('categories-update/<int:pk>', CategoryUpdateView.as_view(), name='admin_categories_update'),
    path('categories-delete/<int:pk>', CategoryDeleteView.as_view(), name='admin_categories_delete'),
    path('products/', ProductListView.as_view(), name='admin_products'),
    path('products-create/', ProductCreateView.as_view(), name='admin_products_create'),
    path('products-update/<int:pk>', ProductUpdateView.as_view(), name='admin_products_update'),
    path('products-delete/<int:pk>', ProductDeleteView.as_view(), name='admin_products_delete'),

]
