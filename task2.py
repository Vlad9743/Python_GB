#Задача 2: Найдите сумму цифр трехзначного числа.

flag = True

while flag:
    inputNumber = input("Input 3-digit number: ")
    if (inputNumber.isdigit() == False):
        print("Input number instead of text.")
    else:
        number = int(inputNumber)
        if (number < 100) or (number > 999):
            print("The number should be 3-digit.")
        else:
            flag = False
            print("Input is correct.")

sum = int(0)

while number != 0:
    sum += number % 10
    number //= 10
print("The sum is: ", sum)
