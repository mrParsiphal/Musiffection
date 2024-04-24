from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import UserProfile
from django import forms

from .validators import validate_test


class LoginForm(forms.Form):
    login = forms.CharField(
        label='Логин',
        max_length=15,
        validators=[validate_test]
    )
    password = forms.CharField(
        label='Пароль',
        strip=False,
        widget=forms.PasswordInput(),
    )

    class Meta:
        model = UserProfile
        fields = ('login', 'password')


class SignUpForm(UserCreationForm):
    login = forms.CharField(
        label='Логин',
        max_length=15,
        help_text='Не более 15 символов. Только буквы кириллицы, цифры и символы .@+-_',
        validators=[validate_test]
    )
    email = forms.EmailField(
        label='Электронная почта',
        max_length=20,
        help_text='!!!!'
    )
    password1 = forms.CharField(
        label='Пароль',
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text='Длина пароля не менее 8 символов. \nПароль должен состоять из символов английского алфавита и цифр.',
    )
    password2 = forms.CharField(
        label='Пароль',
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text='Повторите, пожалуйста, пароль',
    )

    class Meta:
        model = UserProfile
        fields = ('login', 'email', 'password1', 'password2', )


class UserChangeForm(UserChangeForm):

    class Meta:
        model = UserProfile
        fields = ('login', )