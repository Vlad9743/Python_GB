#Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд
#и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, 
#где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, 
#т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

flag = True

while flag:
    ticketNumber = input("Input ticket number: ")
    if (ticketNumber.isdigit() == False):
        print("Input number instead of text.")
    else:
        if (len(ticketNumber) != 6):
            print("Wrong number")
        else:
            flag = False
            print("Input is correct.")

sum1 = int(ticketNumber[0]) + int(ticketNumber[1]) + int(ticketNumber[2])
sum2 = int(ticketNumber[3]) + int(ticketNumber[4]) + int(ticketNumber[5])
if sum1 == sum2:
    print("Ticket number " + ticketNumber + " is LUCKY.")
else:
    print("Ticket number " + ticketNumber + " is NOT LUCKY.")
