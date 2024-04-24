with open('Список жанров музыки.txt', encoding='UTF-8') as list_genres:
    genres = set(list_genres.readlines())
genres_list = []
for genre in genres:
    if genre.lower() not in genres_list:
        i = genre.rstrip().lower().split(maxsplit=1)
        if len(i) > 1:
            genres_list.append(i[0].title() + ' ' + i[1])
        else:
            genres_list.append(i[0].title())
with open('Список жанров музыки.txt', 'w', encoding='UTF-8') as file:
    for genre in genres_list:
        file.write(genre + '\n')