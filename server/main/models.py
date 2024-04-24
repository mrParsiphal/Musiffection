from django.db import models


class Genres(models.Model):
    genre = models.CharField(max_length=50, unique=True, verbose_name='Жанр')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления записи')

    def __str__(self):
        return self.genre

    class Meta:
        verbose_name_plural = 'Жанры'


class Tegs(models.Model):
    teg = models.CharField(max_length=15, unique=True, verbose_name='Название тега')
    creator = models.CharField(max_length=15, unique=True, verbose_name='Создатель тега')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления записи')

    def __str__(self):
        return self.teg

    class Meta:
        verbose_name_plural = 'Теги'


class Musics(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    file = models.CharField(max_length=100, verbose_name='Название музыкального файла')
    img = models.ImageField(upload_to='./musics files/music img', default='main/img/music_1.jpg', max_length=100, verbose_name='Изображение', null=True, blank=True)
    author = models.CharField(default='неизвестен', max_length=100, verbose_name='Автор')
    text = models.TextField(default='Ещё ни кто не добавил слова песни', verbose_name='Слова песни', null=True, blank=True)
    duration = models.CharField(max_length=7, verbose_name='Длительность')
    tegs = models.ManyToManyField(Tegs, verbose_name='Теги', blank=True)
    genres = models.ManyToManyField(Genres, verbose_name='жанры', blank=True)
    rating = models.IntegerField(default=0, verbose_name='Репутация')
    auditions = models.IntegerField(default=0, verbose_name='Количество прослушиваний')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Музыка'


class Ip(models.Model):
    ip = models.CharField(max_length=15, unique=True, verbose_name='Ip адресс')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления записи')

    def __str__(self):
        return self.ip

    class Meta:
        verbose_name_plural = 'Ip'


class Ip_and_Musics(models.Model):
    ip = models.ForeignKey(Ip, on_delete=models.CASCADE, verbose_name='Ip адресс который прослушал музыку')
    music_id = models.ForeignKey(Musics, db_index=True, on_delete=models.CASCADE, verbose_name='Id прослушанной музыки')
    attitude = models.BooleanField(verbose_name='Отношение', null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления записи')

    # def save(self, *args, **kwargs):
    #     if not Invite_code_bindings.objects.filter(user_invite_code=self.user_invite_code,
    #                                                invited_users=self.invited_users).exists(): Чуть позже адаптировать
    #         super(Invite_code_bindings, self).save(*args, **kwargs)

    def __str__(self):
        return f'Прослушивание {self.ip}'

    class Meta:
        verbose_name_plural = 'Прослушивания'


class Authors(models.Model):
    author_id = models.IntegerField(verbose_name='Id', unique=True)
    author = models.CharField(max_length=15, verbose_name='Автор')
    rating = models.IntegerField(default=0, verbose_name='Репутация')
    MP_author = models.BooleanField(default=False, verbose_name='Наиболее популярный')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')

    def __str__(self):
        return self.author

    class Meta:
        verbose_name_plural = 'Авторы'

