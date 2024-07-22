from users import models


def user_avatar(login: str = 'AnonymousUser'):
    if str(login) == 'AnonymousUser':  # Иконка зарегистрированного пользователя или заглушка
        avatarUrl = 'main/img/Stoned_Fox.jpg'
    else:
        avatar_path = models.UserProfile.objects.get(login=login).img.url
        avatarUrl = avatar_path.split('/', 3)[3]
    return avatarUrl