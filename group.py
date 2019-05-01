import re

def get_trailing_number(s):
    m = re.search(r'\d+$', s)
    return int(m.group()) if m else None

def reade_group_list():
 #   f = open('group.txt')
    with open("group.txt") as file:
        array = [row.strip() for row in file]
    return  array

array=reade_group_list()

#for i in array:
#    i=(re.findall('\d+', i ))
[get_trailing_number(i) for i in array]


test='https://vk.com/public176613767'
test=get_trailing_number(test)

print(array)




