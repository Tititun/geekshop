from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import auth, messages
from django.urls import reverse, reverse_lazy
from django.views.generic import FormView

from authapp.forms import UserLoginForm, UserRegisterForm, UserProfileForm

# Create your views here.
from authapp.models import User
from baskets.models import Basket
from geekshop import settings
from mainapp.mixin import BaseClassContextMixin


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = auth.authenticate(username=username, password=password)
            if user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main'))
        else:
            print(form.errors)
    else:
        form = UserLoginForm()
    context = {
        'title': 'Авторизация',
        'form': form
    }
    return render(request, 'authapp/login.html', context)


class RegisterListView(FormView, BaseClassContextMixin):
    model = UserRegisterForm
    template_name = 'authapp/register.html'
    form_class = UserRegisterForm
    title = 'Регистрация'
    success_url = reverse_lazy('auth:login')

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            user = form.save()
            if self.send_verify_link(user):
                messages.set_level(request, messages.SUCCESS)
                messages.success(request, 'Вы успешно зарегистрированы')
                return HttpResponseRedirect(reverse('authapp:login'))
            else:
                messages.set_level(request, messages.ERROR)
                messages.error(request, form.errors)
        return render(request, self.template_name, {'form': form})

    def send_verify_link(self, user):
        verify_link = reverse('authapp:verify', args=[user.email, user.activation_key])
        subject = f'Для активации записи {user.username} пройдите по ссылке'
        message = f'Для подтверждения учетной записи {user.username} на портале Geekshop ' \
                  f'{settings.DOMAIN_NAME}{verify_link}'
        return send_mail(subject, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)

    def verify(self, email, activate_key):
        try:
            user = User.objects.get(email=email)
            if user and user.activation_key == activate_key and not user.is_activation_key_expires():
                user.activation_key = ''
                user.activation_key_expires = None
                user.is_active = True
                user.save()
                auth.login(self, user)
            return render(self, 'authapp/verification.html')
        except Exception as e:
            return HttpResponseRedirect(reverse('main'))


@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(instance=request.user,
                               data=request.POST,
                               files=request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    context = {
        'title': 'Профиль',
        'form': UserProfileForm(instance=request.user)
    }
    return render(request, 'authapp/profile.html', context)


def logout(request):
    auth.logout(request)
    return render(request, 'mainapp/index.html')
