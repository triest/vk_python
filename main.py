#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import vk_api
from vk_api import VkUpload

group_list = []
files_list = []
logins_dictionary = dict()

file_with_logins = 'logins.txt'


def only_numerics(seq):
    return filter(type(seq).isdigit, seq)


# вставка данных в группу
def insert_data_in_group(group_list):
    for item in group_list:

        try:
            vk_session.method("wall.post", {
                'owner_id': item,  # Посылаем себе на стену # c минусом - в группу.
                'message': 'Новый сайт знакомст! Никаких банов и запретов! Ваша анкета всегда доступна! Заходите! http://sakura-city.info/',
                'attachment': attachment,
            })
            print("insert success:" + item)
        except:
            # print("error insert"+item)
            pass


# добавляем данные в лист
def reade_group_list(filename):
    f = open(filename)
    for line in f:
        temp = re.sub("\D", "", line)
        if not temp:
            pass
        else:
            temp = "-" + temp
            group_list.append(temp)


# читает даннные в лист с логинами
def reade_logins_from_file():
    f = open(file_with_logins)
    for line in f:
        line = line[:-1];
        rez = line.split(':');
        print("login:" + rez[0]);
        print("pass:" + rez[1]);
        # надо будет попутаться залогиниться с первым удачным логином
        vk_session = vk_api.VkApi(rez[0], rez[1])
        try:
            vk_session.auth()
            return  True# вурнудись, если получилось
        except:
            return False
            print("login fail")
            # next() #следующая итерация


# читает список файлов
def reade_files_list():
    f = open('files_list.txt')
    for line in f:
        line = line[:-1]
        # print(line)

        reade_group_list(line)  # добавляем данные из файла в мссив

    print(group_list)
    insert_data_in_group(group_list)  # потом для всех файлов



if reade_logins_from_file():
    reade_files_list()
else:
    print("login error")
    exit()
exit()

# Авторизация по логину/паролю (если нужно по токену, заполнять параметр token)
# login, password = 'triest21@gmail.com', 'atmega16'
login, password = '77058973231', 'admincs'

vk_session = vk_api.VkApi(login, password)

try:
    vk_session.auth()
except:
    print("login fail")
    exit(403)

exit()

upload = VkUpload(vk_session)  # Для загрузки изображений

photos = ['new.jpeg']  # картинки, лежат в том-же папке, что и исполняемый
# Или:
# photos = [open('1.jpg', 'rb'), open('2.jpg', 'rb')]
photo_list = upload.photo_wall(photos)
attachment = ','.join('photo{owner_id}_{id}'.format(**item) for item in photo_list)
reade_files_list()

exit()
