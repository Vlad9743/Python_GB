#Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество элементов массива, 
#больших предыдущего (элемента с предыдущим номером)

#Input: [0, -1, 5, 2, 3] 
#Output: 2 (-1 < 5, 2 < 3)

list1 = [0, -1, 5, 2, 3,2,1]
counter = 0

for i in range(1, len(list1)):
    if list1[i] > list1[i-1]:
        counter += 1
print(counter)