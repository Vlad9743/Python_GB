# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и 
# нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, 
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, 
# находясь перед некоторым кустом заданной во входном файле грядки.

numberOfBushes = 8
numberOfBerries = [5, 12, 78, 56, 13, 23, 76, 43]

maxHarvest = numberOfBerries[0] + numberOfBerries[1] + numberOfBerries[2]

numberOfBerries_circled = numberOfBerries
numberOfBerries_circled.append(numberOfBerries[0])
numberOfBerries_circled.append(numberOfBerries[1])
print(numberOfBerries_circled)

for i in range(1, len(numberOfBerries_circled) - 2):
    temp1 = numberOfBerries_circled[i] + numberOfBerries_circled[i+1] + numberOfBerries_circled[i+2]
    if temp1 > maxHarvest:
        maxHarvest = temp1

print("Max possiable harvest: ", maxHarvest)