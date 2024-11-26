from authapp.models import User
from django.shortcuts import render
from django.contrib import messages
from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.views import PasswordResetView, \
    PasswordResetConfirmView
from django.views.generic import CreateView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, \
    reverse
from authapp.forms import UserLoginForm
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
import logging

logger = logging.getLogger('global')

class UserLoginView(LoginView):
    """
    Авторизация пользователя.
    """

    template_name = 'authapp/login.html'
    form_class = UserLoginForm
    redirect_authenticated_user = True


    def form_valid(self, form: UserLoginForm):
        """
        Метод, вызываемый при валидации формы
        """
        super().form_valid(form)
        logger.info(f"Пользователь {self.request.user.username} успешно авторизовался!")
        return HttpResponseRedirect(self.get_success_url())



# class UserLogoutView(LogoutView):
#     """
#     Выход пользователя из учётной записи
#     """
#     next_page = '/'
#
#
# class UserSignUpView(CreateView):
#     """
#     Регистрация пользователя
#     """
#     model = User
#     template_name = 'authapp/registr.html'
#     form_class = UserSignUpForm
#     success_url = reverse_lazy('authapp:login')
#     rep_cart = RepCart()
#
#     def get(self, request, *args, **kwargs) \
#             -> HttpResponse:
#         """
#         Метод для отображения страницы регистрации и формы
#         """
#         form = self.form_class(data=request.GET)
#         if request.user.is_authenticated:
#             return HttpResponseRedirect(reverse('coreapp:index'))
#         return render(request, self.template_name, {'form': form})
#
#     def post(self, request, *args, **kwargs) -> HttpResponse:
#         form = self.form_class(data=request.POST)
#         if form.is_valid():  # форма прошла валидацию
#             user = form.save(commit=False)
#             user.is_active = False  # деактивация пользователя
#             user.activation_key = generate_random_string()
#             user.save()
#             current_site = get_current_site(request)
#             site_name = current_site.name
#             protocol = request.scheme
#             domain = current_site.domain
#             send_verif_link.delay(protocol, domain, site_name, user.email,
#                                   user.activation_key,
#                                   user.first_name, user.last_name)
#             # ссылка создана и отправлено сообщение
#             messages.success(request, messages_dict['reg_success'])
#             return HttpResponseRedirect(reverse('authapp:login'))
#         else:  # при наличии ошибок в форме
#             messages.error(request, *list(form.errors.values()))
#         return render(request, self.template_name, {'form': form})
#
#
# def verify_user(request, **kwargs) -> HttpResponse:
#     """
#     Активация учетной записи
#     :return: Response
#     :rtype: HttpResponse
#     """
#     if request.method == 'GET':
#         email = kwargs.get('email')  # мейл из запроса
#         activate_key = kwargs.get('key')  # ключ из запроса
#         user = User.objects.get(email=email)
#         if user and user.activation_key == activate_key:
#             if not user.is_activation_key_expires:
#                 # если еще не прошло 72 часа
#                 # с момента регистрации и ключи одинаковые
#                 user.activation_key = ""
#                 user.is_active = True  # активация пользователя
#                 user.activation_key_expires = None
#                 user.save()
#                 login(request, user)  # вход в учетную запись
#                 session_products = request.session.get('products')
#                 AddToCart.move_from_session(user, session_products)
#             else:
#                 messages.error(request, messages_dict['activate_error'])
#     return HttpResponseRedirect(reverse('coreapp:index'))
#
#
# class UserPassResetView(PasswordResetView):
#     """
#     Класс для отработки отправки токена для смены пароля на
#     электронную почту.
#     """
#     form_class = UserResetPasswordForm
#     template_name = "authapp/forgot_password.html"
#     from_email = settings.EMAIL_HOST_USER
#     html_email_template_name = "authapp/email/reset_confirm.html"
#     email_template_name = 'authapp/email/reset_confirm.html'
#     success_url = reverse_lazy('authapp:login')
#
#     def form_valid(self, form):
#         """
#         Метод, вызываемый при валидации формы
#         """
#         messages.success(self.request, messages_dict['pass_link'])
#         return super().form_valid(form)
#
#
# class UserPassChangeView(PasswordResetConfirmView):
#     """
#     Класс для смены пароля
#     """
#     form_class = UserSetPasswordForm
#     template_name = "authapp/set_password.html"
#     success_url = reverse_lazy('authapp:login')
#
#     def form_valid(self, form):
#         """
#         Метод, вызываемый при валидации формы
#         """
#         messages.success(self.request, messages_dict['pass_change_success'])
#         return super().form_valid(form)