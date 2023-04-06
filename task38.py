# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. 
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле. 
# 1.Программа должна выводить данные 
# 2.Программа должна сохранять данные в текстовом файле 
# 3.Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека) 
# 4.Использование функций. Ваша программа не должна быть линейной

# Задача 38:  Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных.


def read_file(filename):
    with open(filename, 'r') as data:
        data_array = []
        for line in data:
            item1 = line.replace("\n","").split(",")
            data_array.append(item1)
    return data_array

def write_file(filename, data_array):
    with open(filename, 'w') as data:
        for i in data_array:
            data.write(",".join(i))
            data.write("\n")  
    
def add_item(filename, lastname = "", firstname = "", secondname = "", phone = ""):
    data_array = read_file(filename)
    max_id = 0
    for i in range(1, len(data_array)):
        if max_id < int(data_array[i][0]):
            max_id = int(data_array[i][0])
    next_id = max_id + 1
    lastname = input("Фамилия: ")
    firstname = input("Имя: ")
    secondname = input("Отчество: ")
    phone = input("Телефон: ")
    new_item = [str(next_id), lastname, firstname, secondname, phone]
    data_array.append(new_item)
    write_file(filename, data_array)

    print("Запись добавлена.")

def show_all_items(filename):
    data_array = read_file(filename)
    for i in range(1, len(data_array)):
        print("ID: ", data_array[i][0], " | Фамилия: ", data_array[i][1], " | Имя: ", data_array[i][2], " | Отчество: ", data_array[i][3], " | Телефон: ", data_array[i][4])
    print()
    print("Конец файла.")

def delete_item(filename):
    data_array = read_file(filename)
    id_to_delete = input("Введите номер удаляемой записи: ")
    
    new_data_arr = []
    for i in range(0, len(data_array)):
        if data_array[i][0] != id_to_delete:
            new_data_arr.append(data_array[i])
        else:
            continue

    write_file(filename, new_data_arr)
    print("Запись удалена.")

def modify_item(filename):
    data_array = read_file(filename)
    id_to_modify = str(input("Введите id записи, которую требуется изменить: "))

    new_data_arr = []
    for i in range(0, len(data_array)):
        if data_array[i][0] != id_to_modify:
            new_data_arr.append(data_array[i])
        else:
            old_param = input("Введите старое значение заменяемого параметра: ")
            new_param = input("Введите новое значение заменяемого параметра: ")
            new_item = []
            new_item.append(data_array[i][0])

            for j in range(1, len(data_array[i])):
                if data_array[i][j] == old_param:
                    new_item.append(new_param)
                else:
                    new_item.append(data_array[i][j])
            new_data_arr.append(new_item)

    write_file(filename, new_data_arr)
    print("Запись изменена.")

def find_item(filename):
    search_item = input("Введите id, часть ФИО или телефон: ")
    data_array = read_file(filename)
    print("Поиск ... ")

    find_counter = 0
    for i in range(0, len(data_array)):
        for j in range(0, len(data_array[i])):
            if data_array[i][j] == search_item:
                print(data_array[i])
                find_counter += 1

    print("Конец списка. Всего найдено " + str(find_counter) + " записей.")

def menu():
    print("Телефонный справочник:")
    print("1 - показать записи")
    print("2 - добавить запись")
    print("3 - изменить запись")
    print("4 - удалить запись")
    print("5 - найти запись")
    user_operation = int(input())

    if user_operation == 1:
        show_all_items(filename)
    elif user_operation == 2:
        add_item(filename)
    elif user_operation == 3:
        modify_item(filename)
    elif user_operation == 4:
        delete_item(filename)
    elif user_operation == 5:
        find_item(filename)

filename = "Phones.txt"
menu()