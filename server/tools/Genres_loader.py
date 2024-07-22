import os
import MySQLdb
import mutagen
from format_text import *


def login():
    try:
        from server.server.settings import DATABASES
        print((italic("Подключение к базе данных")))
        host = DATABASES['default']['HOST']
        user = DATABASES['default']['USER']
        password = DATABASES['default']['PASSWORD']
        database = DATABASES['default']['NAME']
    except Exception:
        print((italic("Подключение к базе данных")))
        host = input('Введите адресс БД: ')
        database = input('Введите название БД: ')
        user = input('Введите пользователя: ')
        password = input('Введите пароль: ')
    db = MySQLdb.connect(
        host=host,
        user=user,
        password=password,
        database=database)
    print(italic(green('Подключение успешно')))
    cur = db.cursor()
    table = 'main_genreModel'
    return db, cur, table


def load_genres(db, cur, table):
    with open('Список жанров музыки.txt', encoding='UTF-8') as list_genres:
        genres = set(list_genres.readlines())
    cur.execute(f'''SELECT genre FROM {table}''')
    set_db = set([i[0] for i in cur.fetchall()])
    genres.difference_update(set_db)
    sql_request_data = []
    if len(genres) > 0:
        for genre in genres:
            genre = genre.rstrip()
            print(genre)
            sql_request_data.append(
                f'''("{genre}", SYSDATE())''')
        print(italic('Запрос подготовлен. Отправка запроса...'))
        try:
            sql_request = f'''INSERT INTO {table} (genre, date) VALUES ''' + ', '.join(
                sql_request_data)
            cur.execute(sql_request)
            db.commit()
            print(italic(green(f'Данные успешно добавленны!')))
        except Exception as error:
            print(error)
    else:
        print(yellow('Все жанры уже добавленны!'))


if __name__ == '__main__':
    print(italic('Запуск программы'))
    db, cur, table = login()
    load_genres(db, cur, table)
