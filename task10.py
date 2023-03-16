#Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
#Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
#Выведите минимальное количество монет, которые нужно перевернуть

import random
import array


numbercoins = 10
listOfCoins = ""

for i in range(0, numbercoins):
    listOfCoins += str(random.randint(0, 1))

print("Lisy of coins: " + listOfCoins)

heads = 0
tails = 0

for i in range(0, numbercoins):
    if listOfCoins[i] == "1":
        tails += 1
    else:
        heads += 1
#print(str(heads) + " " + str(tails))

if tails <= heads:
    coinsToTurn = tails
else:
    coinsToTurn = heads

print("Have to turn " + str(coinsToTurn) + " coins.")