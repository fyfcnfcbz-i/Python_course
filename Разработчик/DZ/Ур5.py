"""Напишите программу, которая на вход принимает
два числа A и B, и возводит число А в целую степень B с
помощью рекурсии.
A = 3; B = 5 -> 243 (3⁵)
A = 2; B = 3 -> 8"""

# def fun( x , y ):
#     if y == 0:
#         return 1
#     return fun( x , y - 1) * x

# print(fun(2,0))

"""Задача 2: Напишите рекурсивную функцию sum(a, b),
возвращающую сумму двух целых неотрицательных чисел. Из
всех арифметических операций допускаются только +1 и -1.
Также нельзя использовать циклы.
2 2
4"""

# def sum (a, b):
#     if b == 0:
#         return a
#     elif a == 0:
#         return b
#     return sum (a + 1, b - 1)

# print(sum(7,0))