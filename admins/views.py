from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from admins.forms import UserAdminRegisterForm, UserAdminProfileForm, CategoryForm, ProductForm
from authapp.models import User
from mainapp.models import Product_Category, Product


@user_passes_test(lambda u: u.is_superuser)
def index(request):
    return render(request, 'admins/admin.html')

@user_passes_test(lambda u: u.is_superuser)
def admin_users(request):
    context = {
        'users': User.objects.all()
    }
    return render(request, 'admins/admin-users-read.html', context)

@user_passes_test(lambda u: u.is_superuser)
def admin_users_create(request):
    if request.method == 'POST':
        form = UserAdminRegisterForm(data=request.POST,
                                     files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_users'))
    else:
        form = UserAdminRegisterForm()
    context = {
        'title': 'Admin | Регистрация',
        'form': form
    }
    return render(request, 'admins/admin-users-create.html', context)

@user_passes_test(lambda u: u.is_superuser)
def admin_users_update(request, pk):

    user_select = User.objects.get(pk=pk)

    if request.method == 'POST':
        form = UserAdminProfileForm(data=request.POST,
                                    instance=user_select,
                                    files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_users'))
    else:
        form = UserAdminProfileForm(instance=user_select)
    context = {
        'title': 'Admin | Обновление',
        'form': form,
        'user_select': user_select
    }
    return render(request, 'admins/admin-users-update-delete.html', context)

@user_passes_test(lambda u: u.is_superuser)
def admin_users_delete(request, pk):
    if request.method == 'POST':
        user = User.objects.get(pk=pk)
        user.is_active = False
        user.save()
    return HttpResponseRedirect(reverse('admins:admin_users'))


@user_passes_test(lambda u: u.is_superuser)
def admin_categories(request):
    context = {
        'categories': Product_Category.objects.all()
    }
    return render(request, 'admins/admin-categories-read.html', context)

@user_passes_test(lambda u: u.is_superuser)
def admin_categories_create(request):
    if request.method == 'POST':
        form = CategoryForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_categories'))
    else:
        form = CategoryForm()
    context = {
        'title': 'Admin | Категории',
        'form': form
    }
    return render(request, 'admins/admin-categories-create.html', context)

@user_passes_test(lambda u: u.is_superuser)
def admin_categories_update(request, pk):

    category_select = Product_Category.objects.get(pk=pk)

    if request.method == 'POST':
        form = CategoryForm(data=request.POST,
                            instance=category_select)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_categories'))
    else:
        form = CategoryForm(instance=category_select)
    context = {
        'title': 'Admin | Обновление',
        'form': form,
        'category_select': category_select
    }
    return render(request, 'admins/admin-categories-update-delete.html', context)

@user_passes_test(lambda u: u.is_superuser)
def admin_categories_delete(request, pk):
    if request.method == 'POST':
        category = Product_Category.objects.get(pk=pk)
        category.delete()
    return HttpResponseRedirect(reverse('admins:admin_categories'))


@user_passes_test(lambda u: u.is_superuser)
def admin_products(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'admins/admin-products-read.html', context)

@user_passes_test(lambda u: u.is_superuser)
def admin_products_create(request):
    if request.method == 'POST':
        form = ProductForm(data=request.POST,
                           files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_products'))
    else:
        form = ProductForm()
    context = {
        'title': 'Admin | Товары',
        'form': form
    }
    return render(request, 'admins/admin-products-create.html', context)

@user_passes_test(lambda u: u.is_superuser)
def admin_products_update(request, pk):

    product_select = Product.objects.get(pk=pk)

    if request.method == 'POST':
        form = ProductForm(data=request.POST,
                                    instance=product_select,
                                    files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_products'))
    else:
        form = ProductForm(instance=product_select)
    context = {
        'title': 'Admin | Обновление',
        'form': form,
        'product_select': product_select
    }
    return render(request, 'admins/admin-products-update-delete.html', context)

@user_passes_test(lambda u: u.is_superuser)
def admin_products_delete(request, pk):
    if request.method == 'POST':
        product = Product.objects.get(pk=pk)
        product.delete()
    return HttpResponseRedirect(reverse('admins:admin_products'))