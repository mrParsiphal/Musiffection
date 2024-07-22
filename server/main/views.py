from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework import viewsets
from rest_framework.views import APIView
from random import shuffle

import users.models as users
from .models import MusicModel, AuditionModel
from .subfunctions import user_avatar
from .serializers import MusicSerializer, AuditionSerializer
from .permishions import IsAdminOrReadOnly, IsOwnerOrReadOnly, IsAdminOrPostOrUpdateOnly


def Page_not_found(request, exception):
    return render(request, 'main/404.html', status=404)


class PlayerAPIView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        try:
            first_music = int(request.GET["n"])
        except:
            return render(request, 'main/404.html', status=404)
        ip = request.get_host()
        musicList = list(
            MusicModel.objects.values("id", "name", "file", "img", "duration", "author", "auditions", "rating"))
        first_music = musicList.pop(first_music - 1)
        shuffle(musicList)  # aaaaaaaaaaaaaaaaaaaaaaa
        musicList.insert(0, first_music)  # aaaaaaaaaaaaaaaaaaaaaaa
        musics = {f'track_{i}': musicList[i] for i in range(30)}
        musics['length'] = 30
        return Response(musics)


class AuditionsListAPIView(ListAPIView):
    permission_classes = (IsAdminUser,)
    queryset = AuditionModel.objects.all()
    serializer_class = AuditionSerializer


class AuditionsAPIView(CreateAPIView, UpdateAPIView):
    permission_classes = (IsAdminOrPostOrUpdateOnly,)
    queryset = AuditionModel.objects.all()
    serializer_class = AuditionSerializer

    def post(self, request, **kwargs):
        kwargs['ip'] = request.get_host()
        serializer = AuditionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})

    def update(self, request, **kwargs):
        kwargs['ip'] = request.get_host()

        pk = kwargs.get('pk', None)
        if (pk is None) or ():
            return Response({'error': 'pk is missing'})  #1


class MusicAPIView(viewsets.ModelViewSet):
    queryset = MusicModel.objects.all()
    serializer_class = MusicSerializer



def Index(request):  #главная страница
    content = {}
    try:
        content['first_music'] = int(request.GET["m"])
        print(int(request.GET["m"]))
    except:
        content['first_music'] = 'null'
    music_list = list(
        MusicModel.objects.values("id", "name", "file", "img", "duration", "author", "auditions", "rating"))  #****
    shuffle(music_list)  #Здесь должна работать система рекомендаций!!!!
    for i in range(len(music_list)):
        music_list[i]['serial_number'] = i
    content["cells1"] = music_list[:6]
    content["cells2"] = music_list[6:12]
    content["cells3"] = music_list[12:18]
    content["cells4"] = music_list[18:24]
    content["MP_cells"] = [3, 4, 5, 6]
    content['quantity_musics'] = range(30)
    content['quantity_track_cells'] = range(24)
    content['avatar'] = user_avatar(request.user)
    return render(request, "main/index.html", content)


def Player(request):                                  #"К.О.С.Т.ы.Л.ь"
    try:
        first_music = int(request.GET["m"])
        print(int(request.GET["m"]))
    except:
        first_music = 'null'
    return redirect(f'/?m={first_music}')


def Like(request):
    pass


def Author(request):
    return HttpResponse("Автор")


def Search(request):
    return HttpResponse("Поиск")
