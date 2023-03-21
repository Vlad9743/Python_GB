# Задача 18:
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь вводит натуральное число N – количество элементов в массиве и число,
# которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N.
# Выведите, ближайший к X элемент. Если есть несколько элементов, которые равноудалены от X, 
# выведите наименьший по величине.

# Ввод: 10
# Ввод: 7
# 1 2 1 8 9 6 5 4 3 4
# Вывод: 6

import random

flag = True
while flag:
    inputN = input("Input a length of the array: ")
    inputX = input("Input the desired number: ")
    if inputN.isdigit() and inputX.isdigit():
        N = int(inputN)
        X = int(inputX)
        if N > 0:
            flag = False
        else: 
            print("Wrong numbers.")
    else:
        print("Input numbers instead of text.")

list1 = []
for i in range(N):
    list1.append(random.randint(0, N))

closestNum = list1[1]
difference = abs(X - list1[1])

for i in range(1, N):
    temp1 = abs(X - list1[i])
    if temp1 < difference:
        difference = temp1
        closestNum = list1[i]
    elif temp1 == difference:
        if closestNum > list1[i]:
            closestNum = list1[i]

print(list1)
print("The closest number to " + str(X) + " is " + str(closestNum) + " .")

