
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
            data.write(", ".join(i))
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

def menu():
    print("Телефонный справочник:")
    print("1 - показать записи")
    print("2 - добавить запись")
    print("3 - изменить запись")
    print("4 - удалить запись")
    user_operation = int(input())

    if user_operation == 1:
        show_all_items(filename)
    elif user_operation == 2:
        add_item(filename)

filename = "Phones.txt"
menu()