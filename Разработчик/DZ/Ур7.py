# rstrip

"""Задача 1: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
в порядке
Ввод:                                        Вывод:
пара-ра-рам рам-пам-папам па-ра-па-дам       Парам пам-пам"""

p = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
p = p.split()
# print(p)

res = []
gl = "аоэеиыуёюя"

if len(p) <= 1:
    print ("Количество фраз должно быть больше одной!")
else:
    for i in p:
        count = 0
        for j in i:
            if j in gl:
                count += 1
        res.append(count)
    if max(res) == min(res):
        print("Парам пам-пам")
    else:
        print("Пам парам")

print(res)


# # def count_vowels(Y):
# #     count = sum(1 for i in Y if i in gl)
# #     return count

# # res = list(map(count_vowels, p))
# # print(res)


# # print ("Парам пам-пам" if max(res) == min(res) else "Пам парам")


"""Задача 2: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и
столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте,
почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой
ровно два аргумента, как, например, у операции умножения."""


# def print_operation_table(operation, num_rows = 9, num_columns = 9):
#     if num_rows < 2 or num_columns < 2:
#         print('ОШИБКА! Размерности таблицы должны быть больше 2!')
#     else:
#         for i in range(1, num_rows + 1):
#             row = []
#             for j in range(1, num_columns + 1):
#                 row.append(str(operation(i,j)))
#             print(" ".join(row))

    # for i in range(1, num_rows + 1):
    #     value = []
    #     for j in range(1, num_columns + 1):
    #         value.append(operation(i,j))
    #     string = ''
    #     for k in range(num_columns + 1):
    #         string += str(value[k])
    #         string += ' '
    #     string += str(value[num_columns - 1])
    #     print(string)
    

# print_operation_table(lambda x, y: x * y, 3,3) 

# def print_operation_table(operation, num_rows=9, num_columns=9):
#     result = []
#     if num_rows < 2 or num_columns < 2:
#         print('ОШИБКА! Размерности таблицы должны быть больше 2!')
#     else:
#         for i in range(1, num_rows + 1):
#             for j in range(1, num_columns + 1):
#                 if j != num_columns :
#                     result.append(f'{operation(i, j)} ')
#                 else:
#                     result.append(operation(i, j))
#             result.append('\n')
#         print(''.join([str(i) for i in result[:len(result) - 1]]))
