from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import main.models as models
import users.models as users
from django.db.models import F
from random import shuffle
from main.serializers import Musics


def Page_not_found(request, exception):
    return render(request, 'main/404.html', status=404)


def Index(request):  #главная страница
    content = {}
    music_list = Musics("id", "name", "img", "author")
    shuffle(music_list)                                     #Здесь должна работать система рекомендаций!!!!
    for i in range(len(music_list)):
        music_list[i]['serial_number'] = i
    content["cells1"] = music_list[:6]
    content["cells2"] = music_list[6:12]
    content["cells3"] = music_list[12:18]
    content["cells4"] = music_list[18:24]
    content["MP_cells"] = [3, 4, 5, 6]
    content['quantity_musics'] = range(30)
    content['quantity_track_cells'] = range(24)
    if request.user.is_anonymous:   #Иконка зарегистрированного пользователя или заглушка
        content['avatar'] = 'main/img/Stoned_Fox.jpg'
    else:
        avatar_path = users.UserProfile.objects.get(login=request.user).img.url
        content['avatar'] = avatar_path.split('/', 3)[3]
    return render(request, "main/index.html", content)


def Player(request):       #ПЕРЕДЕЛАТЬ ВСЁ НАФИГ ПОД РАБОТУ С ОТДЕЛЬНОЙ СИСТЕМОЙ РЕКОМЕНДАЦИЙ!!!!!!!
    try:
        first_music = int(request.GET["m"])
    except:
        return Index(request)
    ip = get_client_ip(request)
    music_list = Musics("id", "name", "file", "img", "duration", "author", "auditions", "rating")
    first_music = music_list.pop(first_music - 1)
    shuffle(music_list)  # aaaaaaaaaaaaaaaaaaaaaaa
    music_list.insert(0, first_music)  # aaaaaaaaaaaaaaaaaaaaaaa
    musics = {f'track_{i}': music_list[i] for i in range(30)}
    musics['length'] = 30
    return JsonResponse(musics, status=200)


def Auditions(request,):
    ip = get_client_ip(request)
    if request.method == "POST":
        music_id = request.headers['music-id']
        Write_audition(ip, music_id)
        return JsonResponse({'auditions': models.Musics.objects.get(id__exact=music_id).auditions}, status=200)


def Write_audition(ip, music_id):    #Добавление записи об прослушивании
    values_for_update = {"ip": ip}
    registr_ip, created = models.Ip.objects.update_or_create(ip__exact=ip, defaults=values_for_update) #Добавление
    registr_ip.save()
    if not models.Ip_and_Musics.objects.filter(ip__ip__exact=ip, music_id__id__exact=music_id).exists():
        music_id_query = models.Musics.objects.get(id=music_id)
        ip_query = models.Ip.objects.get(ip=ip)
        print(f'[{datetime.now().replace(microsecond=0)}]', "new music's audition:", music_id_query, '  Ip:', ip)
        registr_relation = models.Ip_and_Musics(ip=ip_query, music_id=music_id_query, attitude=None)
        registr_relation.save()
        models.Musics.objects.filter(id__exact=music_id).update(auditions=F('auditions') + 1)


def Like(request):  #Обработка запроса на изменение отношения к музыке (like, dislike)
    ip = get_client_ip(request)
    if request.method == "POST":
        music_id = request.headers['music-id']
        rating = request.headers['rating']
        ip_id = models.Ip.objects.get(ip__exact=ip).id
        ip_query = models.Ip_and_Musics.objects.get(ip__exact=ip_id, music_id__exact=music_id).attitude
        print(ip_query)
        if ip_query is None:
            if rating == 'true':
                set_rating(ip_id, music_id, True, 1)
            else:
                set_rating(ip_id, music_id, False, -1)
        elif ip_query is True:
            if rating == 'false':
                set_rating(ip_id, music_id, False, -2)
        elif ip_query is False:
            if rating:
                set_rating(ip_id, music_id, True, 2)
        print(f"Like: 'ip': {ip}, 'music_id': {music_id}, 'rating': {rating}")
        return JsonResponse({'rating': models.Musics.objects.get(id__exact=music_id).rating}, status=200)
    return HttpResponse(status=200)


def Mark_audition(request):
    return HttpResponse(status=200)


def Author(request):
    return HttpResponse("Автор")


def Search(request):
    return HttpResponse("Поиск")


def get_client_ip(request):     #Получение Ip адресса из запроса
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def set_rating(ip, music_id, ip_update, music_update):  #Установка отношения к музыке в БД
    print(ip, music_id, ip_update, music_update)
    models.Ip_and_Musics.objects.filter(ip__exact=ip, music_id__exact=music_id).update(attitude=ip_update)
    models.Musics.objects.filter(id__exact=music_id).update(rating=F('rating') + music_update)
