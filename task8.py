#Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
#если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на 
#два прямоугольника).

flag = True

while flag:

    #chocoLenght = int(0)
    #chocoWidth = int(0)
    #breakSize = int(0)

    chocoLenght = input("Input a length of the chocolate: ")
    chocoWidth = input("Input a width of the chocolate: ")
    breakSize = input("How many blocks do you want to take? : ")


    if (chocoLenght.isdigit() == False):
        print("Wrong length.")
    elif (chocoWidth.isdigit() == False):
        print("Wrong width.")
    elif (breakSize.isdigit() == False):
        print("Wrong size.")
    else:
        flag = False
        print("Input is correct.")


totalParts = int(chocoLenght)*int(chocoWidth)

if (int(breakSize) % int(chocoLenght) == 0) and (int(breakSize) < totalParts):
    print("POSSIBLE.")
elif (int(breakSize) % int(chocoWidth) == 0) and (int(breakSize) < totalParts):
    print("POSSIBLE.")
else:
    print("IMPOSSIBLE.")