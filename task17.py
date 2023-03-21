# Дан список чисел. Определите, сколько в нем встречается различных чисел. Input: [1, 1, 2, 0, -1, 3, 4, 4]


list1 = [1,1,2,0,-1,3,4,4]

list2 = []
list2.append(list1[0])

for i in range(len(list1)):
    elem1 = list1.pop()
    addInd = True
    for j in range(len(list2)):
        if elem1 == list2[j]:
            addInd = False
    if addInd:
        list2.append(elem1)
    else:
        continue

print(list1)
print(list2)
print(len(list2))

# set1 = set(list1)
# print(set1)
# print(len(set1))
