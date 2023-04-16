# Функция показывает все контакты в справочнике
import os
def file_path(file_name='phone_data') -> str:
    return os.path.join(os.path.dirname(__file__), f'{file_name}.txt')
def show_contact():
    path = file_path()
    with open(path, 'r+', encoding='utf-8') as file:
        book = file.read()
    return book
# Имя
def input_firstname():
    first = input("Введи имя: ")
    remfname = first[1:]
    firstchar = first[0]
    return firstchar.upper() + remfname
# Фамилия
def input_lastname():
    last = input("Введи фамилию: ")
    remlname = last[1:]
    firstchar = last[0]
    return firstchar.upper() + remlname

# Сохраняем новый контакт
def new_contact():
    path = file_path()
    firstname = input_firstname()
    lastname = input_lastname()
    phoneNum = input("Введи телефон: ")
    contactDetails = (f'[{firstname} {lastname} {phoneNum}]\n')
    with open(path,'a', encoding='utf-8') as file:
        file.write(contactDetails)
    print(contactDetails + "\nКонтакт успешно сохранён!")
# Поиск контакта
def search_contact():
    path = file_path()
    searchname = input("Введите имя для поиска: ")
    remname = searchname[1:]
    firstchar = searchname[0]
    searchname = firstchar.upper() + remname
    with open(path, 'r+', encoding='utf-8') as file:
        filecontents = file.readlines()

    found = False
    for line in filecontents:
        if searchname in line:
            print("Результат:", end=" ")
            print(line)
            found = True
            break
    if found == False:
        print("Не найдено", searchname)

# Изменение контакта


def change_person():
    path = file_path()
    searchname = input("Какой контакт хотите изменить? ")
    remname = searchname[1:]
    firstchar = searchname[0]
    searchname = firstchar.upper() + remname
    with open(path, 'r', encoding='utf-8') as file:
        file_contents = file.readlines()
        found = False
        for line in file_contents:
            if searchname in line:
                print(end=" ")
                print(line)
                found = True
                break
    with open(path, "w", encoding='utf-8') as file:
        for lines in file_contents:
            if line.strip(" ") != lines:
                file.write(lines)
    firstname = input_firstname()
    lastname = input_lastname()
    phoneNum = input("Введи телефон: ")
    contactDetails = ("["+firstname + " " + lastname +
                      ", " + phoneNum + "]\n")
    with open(path, 'a', encoding='utf-8') as file:
        file.write(contactDetails)
    print(contactDetails + "\nКонтакт успешно сохранён!")
    



def delete_contact():
    path = file_path()
    searchname = input("Какое имя хотите удалить? ")
    remname = searchname[1:]
    firstchar = searchname[0]
    searchname = firstchar.upper() + remname
    with open(path, 'r', encoding='utf-8') as file:
        file_contents = file.readlines()
        found = False
        for line in file_contents:
            if searchname in line:
                print("Удалено:", end=" ")
                print(line)
                found = True
                break
    with open(path, "w", encoding='utf-8') as file:
        for lines in file_contents:
            if line.strip(" ") != lines:
                file.write(lines)


def main_menu():
    print("\nМеню\n")
    print("1. Показать все контакты")
    print("2. Добавить новый контакт")
    print("3. Поиск контакта")
    print("4. Изменение контакта")
    print("5. Удаление контакта")
    print("6. Выход")
    choice = input("Введи нужное: ")
    if choice == "1":
        print(show_contact())
        main_menu()
    elif choice == "2":
        new_contact()
        main_menu()
    elif choice == "3":
        print(search_contact())
        main_menu()
    elif choice == "4":
        change_person()
        main_menu()
    elif choice == "5":
        delete_contact()
        main_menu()    
    elif choice == "6":
        print("До свидания!")
    else:
        print("Пожалуйста, предоставьте действительные данные!\n")
        # enter = input("Нажмите Enter, чтобы продолжить ...")
        main_menu()



main_menu()