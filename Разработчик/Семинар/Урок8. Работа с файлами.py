"""Создать телефонный справочник с
возможностью импорта и экспорта данных в
формате .txt. Фамилия, имя, отчество, номер
телефона - данные, которые должны находиться
в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в
текстовом файле
3. Пользователь может ввести одну из
характеристик для поиска определенной
записи(Например имя или фамилию
человека)
4. Использование функций. Ваша программа
не должна быть линейной"""



def work_with_phonebook():
    
    choice = show_menu()

    phone_book = read_txt('file1.txt')


    while (choice!=9):

        if choice==1:
            print_result(phone_book)
        elif choice==2:
            last_name = input('Введите фамилию:  ')
            print(find_by_lastname(phone_book,last_name))
        elif choice==3:
            number = input('Введите номер телефона:  ')
            print(find_by_number(phone_book,number))
        elif choice==4:
            new_fem = input('Введите фамилию:  ')
            new_name = input('Введите имя:  ')
            new_number = input('Введите телефон:  ')
            new_opicanie = input('Введите описание:  ')
            print(add_user(phone_book,new_fem, new_name, new_number, new_opicanie))
        
        elif choice == 5:
            name_or_lastname = input('Введите имя или фамилию для изменения: ')
            print(update_entry(phone_book, name_or_lastname))
        elif choice == 6:
            name_or_lastname = input('Введите имя или фамилию для удаления: ')
            print(delete_entry(phone_book, name_or_lastname))
        
        elif choice==7:
            write_txt('phonebook.txt',phone_book)
            print("Данные сохранены в файл phonebook.txt")

        elif choice==8:
            print("Работа завершена.")
            break


        choice=show_menu()

 # Отображаем меню и получаем выбор пользователя
def show_menu():
    print("\nВыберите необходимое действие:\n" 
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
          "5. Изменить запись\n"
          "6. Удалить запись\n"
          "7. Сохранить справочник в текстовом формате\n"
          "8. Закончить работу")
    choice = int(input())
    return choice


# Чтение данных из текстового файла
def read_txt(filename): 
    phone_book=[]
    fields=['Фамилия', 'Имя', 'Телефон', 'Описание']

    with open(filename,'r',encoding='utf-8') as phb:
        for line in phb:
           record = dict(zip(fields, [field.strip() for field in line.strip().split(',')]))
           phone_book.append(record)	
    return phone_book


# Вывод всех записей справочника
def print_result(phone_book):
    for entry in phone_book:
        print('| '.join(f"{key}: {value}" for key, value in entry.items()))


# Поиск записи по фамилии
def find_by_lastname(phone_book, last_name):
    result = [entry for entry in phone_book if entry['Фамилия'].strip().lower() == last_name.strip().lower()]

    if not result:
        return "Запись не найдена."
    
    formatted_results = '\n'.join('| '.join(f"{key}: {value}" for key, value in entry.items()) for entry in result)
    return formatted_results

# Поиск записи по номеру телефона
def find_by_number(phone_book, number):
    result = [entry for entry in phone_book if entry['Телефон'].strip() == number.strip()]

    if not result:
        return "Запись не найдена."

    formatted_results = '\n'.join('| '.join(f"{key}: {value}" for key, value in entry.items()) for entry in result)
    return formatted_results
  


# Добавление новой записи в справочник
def add_user(phone_book, new_fem, new_name, new_number, new_opicanie):
     new_entry = {
        'Фамилия': new_fem.strip(),
        'Имя': new_name.strip(),
        'Телефон': new_number.strip(),
        'Описание': new_opicanie.strip()
    }
     phone_book.append(new_entry)
     return "Запись успешно добавлена в справочник."


# Функция изменения данных по имени или фамилии
def update_entry(phone_book, name_or_lastname):
    found_entries = []
    for entry in phone_book:
        if entry['Фамилия'].lower() == name_or_lastname.strip().lower() or entry['Имя'].lower() == name_or_lastname.strip().lower():
            found_entries.append(entry)

    if not found_entries:
        return "Запись не найдена."

    print("Найденные записи:")
    for i, entry in enumerate(found_entries, start=1):
        print(f"{i}. {entry['Фамилия']} {entry['Имя']}")

    choice = int(input("Введите номер записи для изменения: "))
    if 1 <= choice <= len(found_entries):
        entry_to_update = found_entries[choice - 1]
        new_number = input("Введите новый номер телефона: ")
        new_description = input("Введите новое описание: ")

        entry_to_update['Телефон'] = new_number.strip()
        entry_to_update['Описание'] = new_description.strip()

        return "Запись успешно изменена."
    else:
        return "Некорректный выбор номера записи."



# Функция удаления данных по имени или фамилии
def delete_entry(phone_book, name_or_lastname):
    found_entries = []
    for entry in phone_book:
        if entry['Фамилия'].lower() == name_or_lastname.strip().lower() or entry['Имя'].lower() == name_or_lastname.strip().lower():
            found_entries.append(entry)

    if not found_entries:
        return "Запись не найдена."

    print("Найденные записи:")
    for i, entry in enumerate(found_entries, start=1):
        print(f"{i}. {entry['Фамилия']} {entry['Имя']}")

    choice = int(input("Введите номер записи для удаления: "))
    if 1 <= choice <= len(found_entries):
        phone_book.remove(found_entries[choice - 1])
        return "Запись успешно удалена."
    else:
        return "Некорректный выбор номера записи."


# Запись данных в текстовый файл
def write_txt(filename , phone_book):
    with open(filename,'w',encoding='utf-8') as phout:
        for i in range(len(phone_book)):
            s=''
            for v in phone_book[i].values():
                s = s + v + ','
            phout.write(f'{s[:-1]}\n')



work_with_phonebook()
