from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone

from .managers import UserManager
from .validators import validate_test


class UserProfile(AbstractBaseUser, PermissionsMixin):
    login = models.CharField(validators=[validate_test], max_length=15, unique=True, verbose_name='Логин')
    name = models.CharField(max_length=15, default='Слушатель', verbose_name='Отображаемое имя')
    email = models.EmailField(max_length=20, unique=True, null=True, blank=True, verbose_name='Электронная почта')
    img = models.ImageField(upload_to='users/static/users/img', default='users/static/users/img/Stoned_Fox.jpg', verbose_name='Изображение', null=True, blank=True)
    authorship = models.BooleanField(default=False, blank=True, verbose_name='Авторство')
    is_active = models.BooleanField(default=True, verbose_name='Активный')
    is_staff = models.BooleanField(default=False, verbose_name='Статус персонала')
    is_superuser = models.BooleanField(default=False, verbose_name='Суперпользователь')
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания аккаунта')
    date_of_change = models.DateTimeField(default=timezone.now, verbose_name='Дата последнего редактирования')

    objects = UserManager()

    USERNAME_FIELD = 'login'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'