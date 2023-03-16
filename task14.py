#Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

numLimit = 31
currentMult = 2

while True:
    if currentMult <= numLimit:
        print(currentMult)
        currentMult *= 2
    else:
        break