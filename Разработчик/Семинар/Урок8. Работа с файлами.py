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


    while (choice!=7):

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
        elif choice==5:
            write_txt('phonebook.txt',phone_book)
            print("Данные сохранены в файл phonebook.txt")

        elif choice==6:
            print("Работа завершена.")


        choice=show_menu()

 # Отображаем меню и получаем выбор пользователя
def show_menu():
    print("\nВыберите необходимое действие:\n" 
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
          "5. Сохранить справочник в текстовом формате\n"
          "6. Закончить работу")
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
        print(', '.join(f"{key}: {value}" for key, value in entry.items()))

# Поиск записи по фамилии
def find_by_lastname(phone_book, last_name):
    result = [entry for entry in phone_book if entry['Фамилия'].strip() == last_name]
    return result if result else "Запись не найдена."

# Поиск записи по номеру телефона
def find_by_number(phone_book, number):
    result = [entry for entry in phone_book if entry['Телефон'].strip() == number]
    return result if result else "Запись не найдена."


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




# def write_txt(filename, phone_book):
#     # Запись данных в текстовый файл
#     with open(filename, 'w', encoding='utf-8') as phout:
#         for entry in phone_book:
#             # Записываем каждую запись в файл
#             phout.write(','.join(entry.values()) + '\n')


# Запись данных в текстовый файл
def write_txt(filename , phone_book):
    with open(filename,'w',encoding='utf-8') as phout:
        for i in range(len(phone_book)):
            s=''
            for v in phone_book[i].values():
                s = s + v + ','
            phout.write(f'{s[:-1]}\n')





work_with_phonebook()


