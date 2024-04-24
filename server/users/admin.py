from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.safestring import mark_safe

from .models import UserProfile
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError


class UserLoginForm(forms.ModelForm):
    pass


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)

    class Meta:
        model = UserProfile
        fields = ('login', )

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserAdmin(BaseUserAdmin):
    add_form = UserCreationForm

    list_display = (
        'login', 'name', 'email', 'authorship', 'is_active', 'is_staff', 'date_joined')
    search_field = ('login', 'email', )
    filter_horizontal = ()
    list_filter = ()
    ordering = ('login',)
    fieldsets = (
        (None, {'fields': ('login', 'password')}),
        ('Личная информация', {'fields': ('name', 'email', 'preview', 'img')}),
        ('Настройки доступа', {'fields': ('is_superuser', 'is_staff', 'is_active', 'date_joined',)}),
        ('Авторство', {'fields': ('authorship',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('login', 'email', 'password1', 'password2'),
        }),
    )
    readonly_fields = ['date_joined', 'preview']

    def preview(self, obj):
        img = obj.img.url.replace('/users', '', 1)
        return mark_safe(f'<img src="{img}" style="max-height: 300px;>')

    preview.short_description = "Изображение"


admin.site.register(UserProfile, UserAdmin)
