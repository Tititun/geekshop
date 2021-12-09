from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from mainapp.mixin import BaseClassContextMixin
from admins.forms import UserAdminRegisterForm, UserAdminProfileForm, CategoryForm, ProductForm
from authapp.models import User
from mainapp.models import Product_Category, Product


@user_passes_test(lambda u: u.is_superuser)
def index(request):
    return render(request, 'admins/admin.html')


class UserListView(ListView, BaseClassContextMixin):
    model = User
    template_name = 'admins/admin-users-read.html'
    context_object_name = 'users'
    title = 'Пользователи'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(UserListView, self).dispatch(request, *args, **kwargs)


class UserCreateView(CreateView, BaseClassContextMixin):
    model = User
    template_name = 'admins/admin-users-create.html'
    form_class = UserAdminRegisterForm
    success_url = reverse_lazy('admins:admin_users')
    context_object_name = 'users'
    title = 'Регистрация'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(UserCreateView, self).dispatch(request, *args, **kwargs)


class UserUpdateView(UpdateView, BaseClassContextMixin):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    form_class = UserAdminProfileForm
    success_url = reverse_lazy('admins:admin_users')
    title = 'Обновление данных пользователя'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(UserUpdateView, self).dispatch(request, *args, **kwargs)


class UserDeleteView(DeleteView, BaseClassContextMixin):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    success_url = reverse_lazy('admins:admin_users')
    title = 'Удалить пользователя'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(UserDeleteView, self).dispatch(request, *args, **kwargs)


class CategoryListView(ListView, BaseClassContextMixin):
    model = Product_Category
    template_name = 'admins/admin-categories-read.html'
    context_object_name = 'categories'
    title = 'Категории'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(CategoryListView, self).dispatch(request, *args, **kwargs)


class CategoryCreateView(CreateView, BaseClassContextMixin):
    model = Product_Category
    template_name = 'admins/admin-categories-create.html'
    form_class = CategoryForm
    success_url = reverse_lazy('admins:admin_categories')
    context_object_name = 'category'
    title = 'Создание категории'


    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(CategoryCreateView, self).dispatch(request, *args, **kwargs)


class CategoryUpdateView(UpdateView, BaseClassContextMixin):
    model = Product_Category
    template_name = 'admins/admin-categories-update-delete.html'
    form_class = CategoryForm
    success_url = reverse_lazy('admins:admin_categories')
    title = 'Обновление данных категории'
    context_object_name = 'category'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(CategoryUpdateView, self).dispatch(request, *args, **kwargs)


class CategoryDeleteView(DeleteView, BaseClassContextMixin):
    model = Product_Category
    template_name = 'admins/admin-categories-update-delete.html'
    success_url = reverse_lazy('admins:admin_categories')
    title = 'Удалить категорию'
    context_object_name = 'category'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(CategoryDeleteView, self).dispatch(request, *args, **kwargs)


class ProductListView(ListView, BaseClassContextMixin):
    model = Product
    template_name = 'admins/admin-products-read.html'
    context_object_name = 'products'
    title = 'Товары'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(ProductListView, self).dispatch(request, *args, **kwargs)


class ProductCreateView(CreateView, BaseClassContextMixin):
    model = Product
    template_name = 'admins/admin-products-create.html'
    form_class = ProductForm
    success_url = reverse_lazy('admins:admin_products')
    context_object_name = 'product'
    title = 'Создание товара'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(ProductCreateView, self).dispatch(request, *args, **kwargs)


class ProductUpdateView(UpdateView, BaseClassContextMixin):
    model = Product
    template_name = 'admins/admin-products-update-delete.html'
    form_class = ProductForm
    success_url = reverse_lazy('admins:admin_products')
    title = 'Обновление данных о товаре'
    context_object_name = 'product'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(ProductUpdateView, self).dispatch(request, *args, **kwargs)


class ProductDeleteView(DeleteView, BaseClassContextMixin):
    model = Product
    template_name = 'admins/admin-products-update-delete.html'
    success_url = reverse_lazy('admins:admin_products')
    title = 'Удалить товар'
    context_object_name = 'product'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(ProductDeleteView, self).dispatch(request, *args, **kwargs)

