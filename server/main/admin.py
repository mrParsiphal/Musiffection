from django.contrib import admin
from .models import Ip, Musics, Ip_and_Musics, Genres, Tegs
from django.utils.safestring import mark_safe


@admin.register(Musics)
class MusicsBAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'id',
        'author',
        'rating',
        'auditions',
        'date',
    ]
    fields = [
        'id',
        'name',
        'author',
        'duration',
        'file',
        'text',
        'rating',
        'auditions',
        'tegs',
        'genres',
        'date',
        'preview',
        'img',
    ]
    readonly_fields = ['id', 'date', 'preview']
    search_fields = ['name', 'pk', ]
    filter_horizontal = ['tegs', 'genres', ]

    def preview(self, obj):
        img = obj.img.url.replace('musics%20files/', '', 1)
        return mark_safe(f'<img src="/static{img}" style="max-height: 300px;>')

    preview.short_description = "Изображение"


@admin.register(Genres)
class GenresBAdmin(admin.ModelAdmin):
    list_display = [
        'genre',
        'date',
    ]
    fields = [
        'genre',
        'date',
    ]
    readonly_fields = ['date']
    search_fields = ['genre']
    filter_horizontal = []


admin.site.register(Ip)
admin.site.register(Tegs)
admin.site.register(Ip_and_Musics)
