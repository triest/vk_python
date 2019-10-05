import datetime


def creat_file():
    ts = datetime.datetime.now()
    print(ts)
    exit()
    f = open('textfile_3.txt', 'tw', encoding='utf-8')
    f.close()


creat_file()