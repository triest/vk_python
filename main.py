#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import vk_api
from vk_api import VkUpload

group_list=[]
files_list=[]

def only_numerics(seq):
    return filter(type(seq).isdigit, seq)

#вставка данных в группу
def insert_data_in_group(group_list):
    for item in group_list:

        try:
            vk_session.method("wall.post", {
                'owner_id': item,  # Посылаем себе на стену # c минусом - в группу.
                'message': 'Новый сайт знкомст! Заходите! http://sakura-city.info/',
                'attachment': attachment,
            })
        except:
            print(item)
            pass

#добавляем данные в лист
def reade_group_list(filename):
    f = open(filename)
    for line in f:
        temp= re.sub("\D", "", line)
        temp="-"+temp
        group_list.append(temp)

        #print(line)

#читает список файлов
def reade_files_list():
    f = open('files_list.txt')
    for line in f:
        line=line[:-1]
        #print(line)
        reade_group_list(line) #добавляем данные из файла в мссив

    #print(group_list)
    insert_data_in_group(group_list) #потом для всех файлов


# Авторизация по логину/паролю (если нужно по токену, заполнять параметр token)
#login, password = 'triest21@gmail.com', 'atmega16'
login, password = '380713943557', 'frdfhbev'

vk_session = vk_api.VkApi(login, password)
vk_session.auth()

upload = VkUpload(vk_session)  # Для загрузки изображений

photos = ['new.jpeg']  #картинки, лежат в том-же папке, что и исполняемый
# Или:
# photos = [open('1.jpg', 'rb'), open('2.jpg', 'rb')]
photo_list = upload.photo_wall(photos)
attachment = ','.join('photo{owner_id}_{id}'.format(**item) for item in photo_list)
reade_files_list()

exit()







#тут будет функция, получающая список групп из  файла


