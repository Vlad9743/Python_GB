# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

numA = int(input("Input number A: "))
numB = int(input("input number B: "))

sum = 0

def sumAB(A, B):
    
    if A == 0:
        return B
    return sumAB(A - 1, B + 1)
    
rez = sumAB(numA, numB)

print("A = " + str(numA) + " , B = " + str(numB) + " -> " + str(rez))