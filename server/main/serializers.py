import main.models as models


def Musics(*args, quantity=None):
    if quantity == None:
        musics = models.Musics.objects.all()
    else:
        musics = models.Musics.objects.all()[:quantity]
    music_list = []
    for music in musics:
        music_parametrs = {arg: str(getattr(music, arg)) for arg in args}
        music_list.append(music_parametrs)
    return music_list