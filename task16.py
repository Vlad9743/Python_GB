#Задача 16:
#Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
#Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X.
#Заполните массив случайными натуральными числами от 1 до N/2.
#Выведите, сколько раз X встречается в массиве.

#Ввод: 5
#Ввод: 1

#1 2 1 2 2
#Вывод: 2

import random

flag = True
while flag:
    inputN = input("Input a length of the array: ")
    inputX = input("Input the desired number: ")
    if inputN.isdigit() and inputX.isdigit():
        N = int(inputN)
        X = int(inputX)
        if N > 0 and X <= N//2:
            flag = False
        else: 
            print("Wrong numbers.")
    else:
        print("Input numbers instead of text.")

counter = 0
list1 = []
for i in range(N):
    list1.append(random.randint(0, N//2))
    if list1[i] == X:
        counter += 1

print(list1)
print("Number " + str(X) + " has been found " + str(counter) + " times.")

