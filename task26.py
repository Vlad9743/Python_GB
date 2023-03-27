#Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

numA = int(input("Input number A: "))
numB = int(input("input number B: "))

def powerAB(A, B):
    
    if B == 0:
        return 1
    return A*powerAB(A, B - 1)
    
if numB < 0 :
    rez = 1 / powerAB(numA, abs(numB))
else: 
    rez = powerAB(numA, numB)

print("A = " + str(numA) + " , B = " + str(numB) + " -> " + str(rez))