import re


def reade_group_list():
 #   f = open('group.txt')
    with open("group.txt") as file:
        array = [row.strip() for row in file]
    return  array

array=reade_group_list()

for i in array:
    i=(re.findall('\d+', i ))

print(i)

