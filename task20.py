# Задача 20:
# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.

# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.

# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

# Ввод: ноутбук
# Вывод: 12

list_en_1 = ["A", "E", "I", "O", "U", "L", "N", "S", "T", "R"]
list_en_2 = ["D", "G"]
list_en_3 = ["B", "C", "M", "P"]
list_en_4 = ["F", "H", "V", "W", "Y"]
list_en_5 = ["K"]
list_en_8 = ["J", "X"]
list_en_10 = [ "Q", "Z"]

list_ru_1 = ["А", "В", "Е", "И", "Н", "О", "Р", "С", "Т"]
list_ru_2 = ["Д", "К", "Л", "М", "П", "У"]
list_ru_3 = ["Б", "Г", "Ё", "Ь", "Я"]
list_ru_4 = ["Й", "Ы"]
list_ru_5 = ["Ж", "З", "Х", "Ц", "Ч"]
list_ru_8 = ["Ш", "Э", "Ю"]
list_ru_10 = ["Ф", "Щ", "Ъ"]

dictionary1 = {}

def addToDictionary(list, point):
    for i in range(len(list)):
        dictionary1[list[i]] = point

addToDictionary(list_en_1, 1)
addToDictionary(list_en_2, 2)
addToDictionary(list_en_3, 3)
addToDictionary(list_en_4, 4)
addToDictionary(list_en_5, 5)
addToDictionary(list_en_8, 8)
addToDictionary(list_en_10, 10)

addToDictionary(list_ru_1, 1)
addToDictionary(list_ru_2, 2)
addToDictionary(list_ru_3, 3)
addToDictionary(list_ru_4, 4)
addToDictionary(list_ru_5, 5)
addToDictionary(list_ru_8, 8)
addToDictionary(list_ru_10, 10)
    
#print(dictionary1)

word = input("Input a word: ")
word = word.upper()

sum = 0
for i in range(len(word)):
    sum += dictionary1.get(word[i], 0)

print("You have " + str(sum) + " points.")