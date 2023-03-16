#Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
#Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки.
#Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

summ = 19
mult = 90
solution = False


for numOne in range(0, 1000):
    if not solution:
        for numTwo in range(0, 1000):
            if (numOne + numTwo == int(summ)) and (numOne * numTwo == int(mult)):
                solution = True
                break
    else: 
        break

print(solution)

if solution:
    print("Number one: " + str(numOne-1) + "; Number two: " + str(numTwo))
else:
    print("No solution")