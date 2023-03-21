#Дана последовательность из N целых чисел и число K.
#Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо,  K – положительное число.

import random

N = 10
K = 3
list1 = []

for i in range(N):
    list1.append(random.randint(0, 9))
print(list1)

for j in range(K):
    a = list1.pop()
    list1.insert(0,a)
print(list1)
