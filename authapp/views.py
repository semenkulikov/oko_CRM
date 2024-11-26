from authapp.models import User
from django.shortcuts import render
from django.contrib import messages
from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.views import PasswordResetView, \
    PasswordResetConfirmView
from django.views.generic import CreateView, DetailView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, \
    reverse
from authapp.forms import UserLoginForm, UserSignUpForm
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
import logging
from django.contrib.auth.mixins import LoginRequiredMixin


logger = logging.getLogger('global')

class UserLoginView(LoginView):
    """
    Авторизация пользователя.
    """

    template_name = 'authapp/login.html'
    form_class = UserLoginForm


    def form_valid(self, form: UserLoginForm):
        """
        Метод, вызываемый при валидации формы
        """
        super().form_valid(form)
        logger.info(f"Пользователь {self.request.user.username} успешно авторизовался!")
        return HttpResponseRedirect(self.get_success_url())

    def post(self, request, *args, **kwargs) -> HttpResponse:
        form = self.form_class(data=request.POST)
        logger.info(f"Попытка авторизации! {form.data.get('username')}: {form.data.get('password')}")
        if form.is_valid():  # форма прошла валидацию
            user = form.get_user()
            login(request, user)
            if user.is_superuser:
                logger.info(f"Администратор {user.first_name} {user.last_name} успешно авторизовался!")
                return HttpResponseRedirect(reverse('admin-panel'))
            else:
                logger.info(f"Пользователь {user.first_name} {user.last_name} успешно авторизовался!")
                return HttpResponseRedirect(reverse('authapp:profile'))
        else:
            messages.error(request, *list(form.errors.values()))
        return render(request, self.template_name, {'form': form})



class UserLogoutView(LogoutView):
    """
    Выход пользователя из учётной записи
    """
    next_page = '/'


class UserSignUpView(CreateView):
    """
    Регистрация пользователя
    """
    model = User
    template_name = 'authapp/registr.html'
    form_class = UserSignUpForm
    success_url = reverse_lazy('authapp:login')

    def get(self, request, *args, **kwargs) \
            -> HttpResponse:
        """
        Метод для отображения страницы регистрации и формы
        """
        form = self.form_class(data=request.GET)
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('index'))
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs) -> HttpResponse:
        form = self.form_class(data=request.POST)
        if form.is_valid():  # форма прошла валидацию
            user = form.save(commit=False)
            user.save()
            logger.info(f'Пользователь {user.first_name} {user.last_name} зарегистрирован')
            return HttpResponseRedirect(reverse('authapp:login'))
        else:  # при наличии ошибок в форме
            messages.error(request, *list(form.errors.values()))
        return render(request, self.template_name, {'form': form})


class ProfileDetailView(LoginRequiredMixin, DetailView):
    """
    View класс для отображения информации об аккаунте
    """
    queryset = User
    template_name = 'authapp/account.html'

    def get_object(self, queryset=None):
        return self.request.user