# Задача №25. Напишите программу, которая принимает на вход строку, и отслеживает, 
# сколько раз каждый символ уже встречался. Количество повторов добавляется к символам с помощью 
# постфикса формата _n.

# Input: a a a b c a a d c d d 
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

stringOne = "a a a b c a a d c d d" 

list1 = stringOne.split(" ")


#print(list1)
#print(len(list1))

dict1 = {}

dict1[list1[0]] = 1

for i in range (1, len(list1)):
    temp1 = dict1.get(list1[i], 0)
    if temp1 == 0:
        dict1[list1[i]] = 1
    else:
        dict1[list1[i]] = temp1 + 1
        list1[i] = list1[i] + "_" + str(temp1)
        
print(dict1)
print(list1)
