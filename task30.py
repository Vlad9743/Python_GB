# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

firstElem = int(input("Input first element: "))
progressDiff = int(input("Input element difference: "))
elemQuantity = int(input("Input elements quantity: "))

list1 = [(firstElem + (i-1) * progressDiff) for i in range(1, elemQuantity + 1)]

print(list1)
