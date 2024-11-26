from django import forms
from authapp.models import User
from django.contrib.auth.forms import AuthenticationForm, \
    UserCreationForm, UsernameField, SetPasswordForm, \
    PasswordResetForm
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from django.template import loader



class UserLoginForm(AuthenticationForm):
    """
    Форма для авторизации пользователя
    """
    username = UsernameField(
        widget=forms.TextInput()
    )
    password = forms.CharField()


    class Meta:
        model = User
        fields = ('username', 'password')


    # def clean(self):
    #     """
    #     Переопределение метода для отображения ошибки при неактивном
    #     пользователе
    #     """
    #     username = self.cleaned_data.get("username")
    #     password = self.cleaned_data.get("password")
    #     if username is not None and password:
    #         self.user_cache = authenticate(
    #             self.request, username=username, password=password
    #         )
    #         if self.user_cache is None:
    #             try:  # попытка найти пользователя с таким email
    #                 user_not_active = User.objects.get(email=username)
    #             except ObjectDoesNotExist:
    #                 user_not_active = None
    #             if user_not_active is not None and \
    #                     user_not_active.check_password(password):
    #                 # если пользователь с таким username(email) существует,
    #                 # и введён верный пароль, но его учетная запись неактивна
    #                 self.confirm_login_allowed(user_not_active)
    #             else:
    #                 raise self.get_invalid_login_error()
    #     return self.cleaned_data


class UserSignUpForm(UserCreationForm):
    """
    Форма для регистрации пользователя
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['placeholder'] = 'E-mail'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget. \
            attrs['placeholder'] = 'Password confirmation'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Surname'
        self.fields['middle_name'].widget.attrs['placeholder'] = 'Middle name'
        self.fields['last_name'].required = True
        self.fields['first_name'].required = True
        for name_field, field in self.fields.items():
            field.widget.attrs['class'] = 'user-input'

    class Meta:
        model = User
        fields = ('email', 'first_name',
                  'middle_name', 'last_name')


