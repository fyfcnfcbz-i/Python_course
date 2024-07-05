# словарь
dict = {333:2, (1, 2):3, "serw":[1,2]}
print(dict)
for i in dict:
    print(i,dict[i]) # ключ, значение ключа

for i in dict.values(): # values - метод выдающиц только значение ключей
    print(i)

for i in dict.items(): # items - метод выдающей выражение из ключа и значения
    print(i)

for i, j in dict.items(): # распакованное значение ключа и значения
    print(i, j)