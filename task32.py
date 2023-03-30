# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
#  (т.е. не меньше заданного минимума и не больше заданного максимума)

import random

list1 = [random.randint(1,20) for i in range(20)]
print(list1)

searchMin = int(input("Input minimum: "))
searchMax = int(input("Input maximum: "))

list2 = []
for i in range(0, len(list1)):
    if list1[i] >= searchMin and list1[i] <= searchMax:
        list2.append(i)

print(list2)

#то же самое генератором списка
list3 = [i for i in range(0, len(list1)) if list1[i] >= searchMin and list1[i] <= searchMax]
print(list3)