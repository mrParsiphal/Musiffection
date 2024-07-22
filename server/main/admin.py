from django.contrib import admin
from .models import IpModel, MusicModel, AuditionModel, GenreModel, TegModel
from django.utils.safestring import mark_safe


@admin.register(MusicModel)
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
        'owner',
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


@admin.register(GenreModel)
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


admin.site.register(IpModel)
admin.site.register(TegModel)
admin.site.register(AuditionModel)
