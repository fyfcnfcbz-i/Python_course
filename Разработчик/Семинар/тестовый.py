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

def read_txt(filename):
    phone_book = []
    fields = ['Фамилия', 'Имя', 'Отчество', 'Телефон', 'Описание']

    with open(filename, 'r', encoding='utf-8') as phb:
        for line in phb:
            record = dict(zip(fields, [field.strip() for field in line.strip().split(',')]))
            phone_book.append(record)

    return phone_book

def write_txt(filename, phone_book):
    with open(filename, 'w', encoding='utf-8') as phout:
        for entry in phone_book:
            phout.write(','.join(entry.values()) + '\n')

def print_result(phone_book):
    for entry in phone_book:
        print(f"Фамилия: {entry['Фамилия']}, Имя: {entry['Имя']}, Отчество: {entry['Отчество']}, Телефон: {entry['Телефон']}, Описание: {entry['Описание']}")

def find_by_lastname(phone_book, last_name):
    result = [entry for entry in phone_book if entry['Фамилия'].strip() == last_name]
    return result if result else "Запись не найдена."

def find_by_number(phone_book, number):
    result = [entry for entry in phone_book if entry['Телефон'].strip() == number]
    return result if result else "Запись не найдена."

def add_user(phone_book, user_data):
    fields = ['Фамилия', 'Имя', 'Отчество', 'Телефон', 'Описание']
    entry = dict(zip(fields, [field.strip() for field in user_data.split(',')]))
    phone_book.append(entry)

def work_with_phonebook():
    choice = show_menu()
    phone_book = read_txt('fail1.txt')

    while choice != 6:
        if choice == 1:
            print_result(phone_book)
        elif choice == 2:
            last_name = input('Введите фамилию: ')
            print(find_by_lastname(phone_book, last_name))
        elif choice == 3:
            number = input('Введите номер телефона: ')
            print(find_by_number(phone_book, number))
        elif choice == 4:
            user_data = input('Введите новые данные (Фамилия, Имя, Отчество, Телефон, Описание): ')
            add_user(phone_book, user_data)
        elif choice == 5:
            write_txt('phonebook.txt', phone_book)
            print("Данные сохранены в файл phonebook.txt")

        choice = show_menu()

work_with_phonebook()
