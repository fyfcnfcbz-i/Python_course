"""факториал числа через рекурсию. A 1...n"""


# def fact(n):
#     if n == 0:
#         return 1
#     return n * fact((n - 1))
    
# print(fact(5))


"""Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1). Требуется найти N-е число Фибоначчи
Input: 7 Output: 21
Задание необходимо решать через рекурсию"""

# def fib(n):
#     if n in [1, 2]:
#         return 1
#     return fib(n - 1) + fib(n - 2)
# print(fib(7))

# list_1 = []
# for i in range(1,10):
#     list_1.append(fib(i))
# print(list_1) # [1, 1, 2, 3, 5, 8, 13, 21, 34]

"""Дано натуральное число N и
последовательность из N элементов.
Требуется вывести эту последовательность в
обратном порядке.
Примечание. В программе запрещается
объявлять массивы и использовать циклы
(даже для ввода и вывода).
Input: 2 -> 3 4
Output: 4 3"""

# def fun(n):
#     if n <= 0:
#         return ''
#     num = input("введите число: ")
#     return fun (n - 1) + ' ' + num

# print(fun(4))
