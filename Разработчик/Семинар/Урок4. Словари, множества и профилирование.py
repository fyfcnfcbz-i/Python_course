# st = '8 7 f     d'
# print(st) # 8 7 f d

# st = st.split()
# print(st) # ['8', '7', 'f', 'd']

# st = st.split(' ')
# print(st)  # ['8', '7', 'f', '', '', '', '', 'd']

# st = st.replace(" ",'-').split(' ') # метод replace перезапись пробелов на -
# print(st) # ['8-7-f-----d']


"""Напишите программу, которая принимает на вход
строку, и отслеживает, сколько раз каждый символ
уже встречался. Количество повторов добавляется к
символам с помощью постфикса формата _n.
Input: a a a b c a a d c d d
Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
Для решения данной задачи используйте функцию.split()"""

# dict = {}
# string = "a a a b c a a d c d d"
# string_res = ""

# for i in string.split():
#     if i in dict:
#         string_res = string_res + i + "_" + str(dict[i]) + " "
#         # dict[i] = dict[i] + 1
#     else:
#         # dict[i] = 1
#         string_res = string_res + i + " "
#     dict[i] = 1 + dict.get(i, 0) # метод get
# print(string_res)


"""Пользователь вводит текст(строка). Словом
считается последовательность непробельных
символов идущих подряд, слова разделены одним
или большим числом пробелов. Определите, сколько
различных слов содержится в этом тексте.
Input: She sells sea shells on the sea shore The shells
that she sells are sea shells I'm sure.So if she sells sea
shells on the sea shore I'm sure that the shells are sea
shore shells
Output: 13"""

text = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"

text = text.upper()
text = text.replace(".",' ').split()
print(text)
print(len(set(text)))




