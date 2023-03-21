# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

import random

flag = True
while flag:
    inputFirstArraySize = input("Input a size of the first array: ")
    inputSecondArraySize = input("Input a size of the second array: ")

    if inputFirstArraySize.isdigit() and inputSecondArraySize.isdigit():
        flag = False
        firstArraySize = int(inputFirstArraySize)
        secondArraySize = int(inputSecondArraySize)
    else:
        print("Input numbers instead of text.")

flag1 = True
while flag1:
    numbers1 = input("Fill first array. Input " + str(firstArraySize) + " numbers divided by spaces: ")
    list1 = numbers1.split(" ")
    checkSum1 = 0
    for i in range(len(list1)):
        checkSum1 += int(list1[i].isdigit())
    if checkSum1 == firstArraySize:
        flag1 = False
    else:
        print("Wrong quantity or format.")

flag2 = True
while flag2:
    numbers2 = input("Fill second array. Input " + str(secondArraySize) + " numbers divided by spaces: ")
    list2 = numbers2.split(" ")
    checkSum2 = 0
    for i in range(len(list2)):
        checkSum2 += int(list2[i].isdigit())
    if checkSum2 == secondArraySize:
        flag2 = False
    else:
        print("Wrong quantity or format.")

#set1 = set(list1)
#set2 = set(list2)
list3 = []

for i in range(len(list1)):
    for j in range(len(list2)):
        if list1[i] == list2[j]:
            list3.append(list1[i])

list3.sort()
set1 = set(list3)
print(set1)