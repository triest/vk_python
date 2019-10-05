#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import vk_api
from vk_api import VkUpload

group_list = []
files_list = []

success = []
error = []


def only_numerics(seq):
    return filter(type(seq).isdigit, seq)


# вставка данных в группу
def insert_data_in_group(group_list):
    count = 1
    group_count = 0
    for item in group_list:
        count = count + 1
        group_count = group_count + 1
        if (count > 10):
            print(group_count)
            count = 0
        try:
            vk_session.method("wall.post", {
                'owner_id': item,  # Посылаем себе на стену # c минусом - в группу.
                'message': 'Новый сайт знакомст! Никаких банов и запретов! Ваша анкета всегда доступна! Заходите! http://sakura-city.info/',
                'attachment': attachment,
            })
            #print("success"+ item)
            success.append(item)
        except:
            #print(item)
            error.append(item)
            pass


# добавляем данные в лист
def reade_group_list(filename):
    f = open(filename)
    for line in f:
        temp = re.sub("\D", "", line)
        temp = "-" + temp
        group_list.append(temp)

        # print(line)




# читает список файлов
def reade_files_list():
    f = open('files_list.txt')
    for line in f:
        line = line[:-1]
        # print(line)
        reade_group_list(line)  # добавляем данные из файла в мссив

    #print(group_list)

login, password = '77058973231', 'admincs'

vk_session = vk_api.VkApi(login, password)
try:
    vk_session.auth()
except:
    print("login fail")
    exit(403)


reade_files_list()
print(group_list)
insert_data_in_group(group_list)  # потом для всех файлов
print("sucess ")
print(*success)

print("error ")
print(*error)

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

upload = VkUpload(vk_session)  # Для загрузки изображений

photos = ['new.jpeg']  # картинки, лежат в том-же папке, что и исполняемый
# Или:
# photos = [open('1.jpg', 'rb'), open('2.jpg', 'rb')]
photo_list = upload.photo_wall(photos)
attachment = ','.join('photo{owner_id}_{id}'.format(**item) for item in photo_list)
reade_files_list()

print("sucess ")


print("error ")

exit()
