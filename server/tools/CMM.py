import os
import shutil
import MySQLdb
from format_text import *


list_app_migrations = ['main', 'users']


def login():
    try:
        from server.server.settings import DATABASES
        print((italic("Подключение к базе данных")))
        host = DATABASES['default']['HOST']
        user = DATABASES['default']['USER']
        password = DATABASES['default']['PASSWORD']
        database = DATABASES['default']['NAME']
    except Exception:
        print((italic(red("Не удалось использовать данные пользователя из файла settings.py!"))))
        host = input('Введите адресс БД: ')
        database = input('Введите название БД: ')
        user = input('Введите пользователя: ')
        password = input('Введите пароль: ')
    db = MySQLdb.connect(
        host=host,
        user=user,
        password=password)
    print(italic(green('Подключение успешно')))
    cur = db.cursor()
    return database, cur




def Cleanup_mysql(database, cur):
    print(italic('Очистка базы данных'))
    cur.execute(f'''DROP DATABASE {database}''')
    cur.execute(f'''CREATE DATABASE {database}''')
    print(italic(green('База данных очищена!')))


def Cleanup_migrations():
    print(italic('Очистка миграций'))
    for path in list_app_migrations:
        files = os.listdir(f'../{path}/migrations')
        for file in files:
            if file not in '__init__.py':
                try:
                    os.remove(f'../{path}/migrations/{file}')
                except:
                    shutil.rmtree(f'../{path}/migrations/{file}')
    print(italic(green('Миграции удалены!')))


if __name__ == '__main__':
    print(italic(red('Вы уверенны, что хотите очистить всю базу данных и все миграции???')))
    answer = input(italic('(Y/N): '))
    if answer.lower() == 'y':
        database, cur = login()
        Cleanup_mysql(database, cur)
        Cleanup_migrations()
