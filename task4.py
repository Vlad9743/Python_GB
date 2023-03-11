#Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. 
#Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, 
#что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

flag = True

while flag:
    inputBirds = input("Input number of paper birds: ")
    if (inputBirds.isdigit() == False):
        print("Input number instead of text.")
    else:
        birds = int(inputBirds)
        if (birds % 6 != 0):
            print("Wrong number")
        else:
            flag = False
            print("Input is correct.")

petiaBirds = birds // 6
serejaBirds = petiaBirds
katiaBirds = 4 * petiaBirds

print("Total birds: ", birds)
print("Peter's birds: ", petiaBirds)
print("Sergei's birds: ", serejaBirds)
print("Kate's birds: ", katiaBirds)