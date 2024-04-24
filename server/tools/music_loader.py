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
    table = 'main_Musics'
    db = MySQLdb.connect(
        host=host,
        user=user,
        password=password,
        database=database)
    print(italic(green('Подключение успешно')))
    cur = db.cursor()
    return db, cur, table


def show_tables(cur):
    try:
        cur.execute('''SHOW TABLES''')
        print(cur.fetchall())
    except Exception as error:
        print(red(error))


def load_music(db, cur, table):
    musics_path = input('Введите путь к файлам: ')
    if musics_path in '':
        musics_path = '../musics files/musics/'
    music_img_path = '../musics files/music img/'
    set_files = set(os.listdir(musics_path))
    cur.execute(f'''SELECT file FROM {table}''')
    set_db = set([i[0] for i in cur.fetchall()])
    set_files.difference_update(set_db)
    cur.execute(f'''SELECT MAX(id) FROM {table}''')
    music_id = cur.fetchall()[0][0]
    if music_id == None:
        music_id = 0
    if len(set_files) > 0:
        sql_request_data = []
        dict_img_files = {}
        for img_file in os.listdir(music_img_path):
            key, value = img_file.rsplit('.', 1)
            dict_img_files[key] = value
        quantity_incorrect_tracks = 0
        for music in set_files:
            mutagen_data = mutagen.File(musics_path + '/' + music)
            if len(music.split(' - ')) == 2 and music.endswith('.mp3'):
                print(green(music))
                music_id += 1
                author, music_name = music[:-4].split(' - ')
                name_music_file = music.rsplit('.', 1)[0]
                if dict_img_files.get(name_music_file) is not None:
                    img_path = 'music img/' + name_music_file + '.' + dict_img_files[name_music_file]
                else:
                    img_path = 'main/img/music_1.jpg'
                sec_dur = mutagen_data.info.length
                duration = f'{int(sec_dur // 60)}'.rjust(2, '0') + ':' + f'{int(sec_dur % 60)}'.rjust(2, '0')
                sql_request_data.append(
                    f'''("{music_id}", "{music_name}", "{music}", "{img_path}", "{author}", "{duration}", 0, 0, SYSDATE())''')
            else:
                print(yellow(music))
                quantity_incorrect_tracks += 1
        if len(sql_request_data) != 0:
            try:
                print(italic('Запрос подготовлен. Отправка запроса...'))
                sql_request = f'''INSERT INTO {table} (id, name, file, img, author, duration, auditions, rating, date) VALUES ''' + ', '.join(
                    sql_request_data)
                cur.execute(sql_request)
                db.commit()
                print(italic(green(f'Данные успешно добавленны!\nКоличество добавленных треков: {len(sql_request_data)}')),
                      italic(yellow(f'\nКоличество некорректных треков: {quantity_incorrect_tracks}')))
            except Exception as error:
                print(error)
        else:
            print(italic(yellow(f'Новые треки не найдены!\nКоличество некорректных треков: {quantity_incorrect_tracks}')))
    else:
        print(italic(yellow('Новые треки не найдены!')))


if __name__ == '__main__':
    print(italic('Запуск программы'))
    db, cur, table = login()
    load_music(db, cur, table)
