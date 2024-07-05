# Инструкция по языку Python

### Создание среды 
```sh
python -m venv .folder
```

Запуск через
- кнопку
- кс 
```sh
python <название файла>
```

% - остаток от деления

// - целочисленное деление

** - возведение в степень
___

**Отступы** (отделение блоков кода )
- TAB
- 4 пробела
___

## else - if -> **elif**
```sh
if .. #если условие верно, то на этом останавливаемся и не переходик на строку elif
    ...
elif ...
    ..
else .. # если все услови оказались неверными
    ... 
```


## Сложные условия(and, or, not)

```sh
if condition1 and condition2: # выполняется когда оба условия окажутся верными
    operator
if condition3 or condition4: # выполняется когда одно из условий окажется верным
    operator
```

## Функция range()
*по умолчанию шаг 1*

r = range(5) -> 0 1 2 3 4  

r = range(2, 5) -> 2 3 4 

r = range(0, -5) -> ----

r = range(1, 10, 2) -> 1, 3, 5, 7, 9 (шаг = 2)

## Строки

```sh
text = 'Привет мир'
print(len(text)) # функция len - позволяет узнать размер  строки
print('мир' in text) # есть ли слово "мир" в строке -> True/Folse
print(text.lower()) # функция lower - перевод заглавных букв в нижний регистр
print(text.upper()) # функция upper -  всех букв в верхний регистр
print(text.replace('мир', 'люди')) # замена слова 
```
## Срезы
**строки имеют индексцию**
```sh
text = 'Привет мир'
print(text[0]) # -> П

print(text[len(text)-1]) # вывод последней буквы из строки -> p
print(text[-1]) # индексация начнется с обратной стороны строки -> р

print(text[:2]) # вывод элемента с 0 по 2 -> Пр
print(text[5:]) # вывод элемента с 5 до конца
print(text[2:7]) # вывод элемента со 2 по 7
print(text[2:-3]) # вывод элемента со 2 по -3
print(text[0:len(text):3]) # идем от начала строки до конца с шагом - 3
print(text[::3])
```
##  Коллекции данных. Профилирование и отладка

### Списки 
```sh
list = [] -> пустой список 
list = list()
list = [1, 2, 3]

print(list) -> результат вывода [1, 2, 3]
print(*list) -> результат вывода 1 2 3
```

```sh
for i in list:
    print(i)
```

-> функция len - длина списка(3)
```sh
print(len(list)) 
```
-> обращение к элементу списка
```sh
print(list[0]) -> 1

print(list[-1]) -> 3
```

-> добавление элемента в список **(append)**
```sh
list = [1, 2, 3]

list.append(8) -> [1, 2, 3, 8]
```

**Основный функции в списках**

- Удаление последнего элемента списка **(pop)**
```sh
list = [1, 2, 3]

print(list.pop()) -> [1, 2]
```
- Удаление конкретного элемента из списка **(pop())**
```sh
list = [1, 2, 3]

print(list.pop(0)) -> [2, 3]
```
- Добавление элемента на нужную позицию **(insert)**
```sh
list = [1, 2, 3]

print(list.insert(0, 7)) -> [7, 1, 2, 3] первое значение - позиция, второе - элемент
```

**Срезы в списках**

```sh
list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list_1[0]) # 1
print(list_1[1]) # 2
print(list_1[len(list_1)-1]) # 10
print(list_1[-5]) # 6
print(list_1[:]) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list_1[:2]) # [1, 2]
print(list_1[len(list_1)-2:]) #[9, 10]
print(list_1[2:9]) # [3, 4, 5, 6, 7, 8, 9]
print(list_1[6:-18]) # []
print(list_1[0:len(list_1):6]) # [1, 7]
print(list_1[::6]) # [1, 7]
```

### Кортеж 
(неизменяемый список)

```sh
t = () # создание пустого кортежа

print(type(t)) # class <'tuple'>

t = (1)
print(type(t)) # class <'int'>

t = (1,)
print(type(t)) # class <'tuple'>



v = [28, 9, 1990]
print(type(v)) # class <'list'> [28, 9, 1990]

v = (type(v))
print(type(v)) # class <'tuple'> (28, 9, 1990)



a, b = 1, 2 # множественное присваивание

a, b, c = v
print (a, b, c) # 28 9 1990 (распаковка кортежа)
```

Вывод кортежа по индексам
```sh
t = (1, 2, 3, 4, )
print(t[1]) # 2
```

Проход по элементам кортежа 
```sh
for i in t
    print(i)


for i in range(len(t))
    print(t[i])  
```
### Словари 
(неупорядоченные коллекции произвольных объектов с доступом по ключу)

```sh
d = {} # создание пустого словаря
d = dict()

d['q'] = 'qwerty'
print(d)         # {'q': 'qwerty'} ключ q со значение qwerty

d['w'] = 'werty'
print(d)         # {'q': 'qwerty', 'w': 'werty'} 

print(d['q'])    # qwerty
```

```sh
dictionary = {}
dictionary ={'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}

print(dictionary['left']) # ←
# типы ключей могут отличаться
print(dictionary['up']) # ↑
# типы ключей могут отличаться
dictionary['left'] = '⇐'
print(dictionary['left']) # ⇐

print(dictionary['type']) # KeyError: 'type'


del dictionary['left'] # удаление элемента


for item in dictionary: 
# for (k,v) in dictionary.items():
print('{}: {}'.format(item, dictionary[item]))
# up: ↑
# down: ↓
# right: →
```
```sh
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
```


### Множества 
(содержат в себе уникальные элементы, не обязательно упорядоченные)

Создание множества
```sh
m = set()
```

```sh
colors = {'red', 'green', 'blue'}
print(colors) # {'red', 'green', 'blue'}

colors.add('red') ->  функция add - добавление значения
print(colors)     # {'red', 'green', 'blue'}
colors.add('gray')
print(colors)     # {'red', 'green', 'blue','gray'}

colors.remove('red') -> функция remove - удаление значения
print(colors)        # {'green', 'blue','gray'}
colors.remove('red') # KeyError: 'red'

colors.discard('red') -> функция discard - проверяет есть ли значение в множистве (если есть - удаляет, нет - пропускает)
print(colors) # {'green', 'blue','gray'}

colors.clear() -> функция clear - удаляет все множество # { }
print(colors) # set()

```
Преобразование списка во множество
```sh
list = [1, 2, 3]
print(set(list))
```

**Операции со множествами**

```sh
a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}

c = a.copy() # c = {1, 2, 3, 5, 8}

u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21} объединение

i = a.intersection(b) # i = {8, 2, 5} пересечение

dl = a.difference(b) # dl = {1, 3} разность
dr = b.difference(a) # dr = {13, 21}

q=a.union(b).difference(a.intersection(b)) # {1, 21, 3, 13}

```

**Замороженное множество**
```sh
a = {1, 2, 3, 5, 8}
b = frozenset(a)
print(b) # frozenset({1, 2, 3, 5, 8})
```

### Генератор спсиков  (List Comprehension)

```sh
list_1 = [exp for item in iterable]
```
```sh
list_1 = [exp for item in iterable (if conditional)]
```
Создать список, состоящий из четных чисел в диапазоне от 1 до 100
```sh
list_1 = []
for i in range(1, 101):
    list_1.append(i)
print(list_1) # [1, 2, 3,..., 100]
```
```sh
list_1 = [i for i in range(1, 101)] # [1, 2, 3,..., 100]
```
Добавить условие (только чётные числа)
```sh
list_1 = [i for i in range(1, 101) if i % 2 == 0] # [2, 4, 6,..., 100]
```
Допустим, вы решили создать пары каждому из чисел (кортежи)
```sh
list_1 = [(i, i) for i in range(1, 101) if i % 2 == 0] # [(2, 2), (4, 4),...,
(100, 100)]
```
Также можно умножать, делить, прибавлять, вычитать. Например, умножить
значение на 2.
```sh
list_1 = [i * 2 for i in range(10) if i % 2 == 0]
print(list_1) # [0, 4, 8, 12, 16]
```

## Функции, рекурсия, алгоритмы

### Функция

```sh
def function_name(x):
    # body line 1
        # ...
    # body line n
    # optional return
```

```sh
def sumNumbers(n):
    summa = 0
    for i in range(1, n + 1):
        summa += i
    # print(summa)
    return summa
# sumNumbers(5)
print(sumNumbers(5))
```

```sh
def sum(*args) # * - неограниченное колличесвто аргументов
    res = ""
    for item in args:
        res += item
    return res

```

### Модульность
импортирование функций 
- создается файл (modul1.py) с функцией(def max1)
- в новом файле 

```sh
import madul1

print(modul1.max1(5, 9))
```
переименовать модуль madul1 как m1
```sh
import madul1 as m1

print(m1.max1(5, 9))
```

импорт на прямую
```sh
from modul1 import max1

print(max1(5, 9))
```
импорт всех функций
```sh
from modul1 import *

print(max1(5, 9))
```

### Рекурсия

```sh
def fib(n):
    if n in [1, 2]:
        return 1
    return fib(n - 1) + fib(n - 2)

list_1 = []
for i in range(1, 10):
    list_1.append(fib(i))
print(list_1) # [1, 1, 2, 3, 5, 8, 13, 21, 34]

```

### Алгоритмы

**Быстрая сортировка**
```sh
def quicksort(array):
    if len(array) < 2:
        return array
    else:
    pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)
print(quicksort([10, 5, 2, 3]))
```
```sh
● 1-е повторение рекурсии:
○ array = [10, 5, 2, 3]
○ pivot = 10
○ less = [5, 2, 3]
○ greater = []
○ return quicksort([5, 2, 3]) + [10] + quicksort([])
● 2-е повторение рекурсии:
○ array = [5, 2, 3]
○ pivot = 5
○ less = [2, 3]
○ greater = []
○ return quicksort([2, 3]) + [5] + quicksort([]) # Важно! Не забывайте, что
здесь помимо вызова рекурсии добавляется список [10]
● 3-е повторение рекурсии:
○ array = [2, 3]
○ return [2, 3] # Сработал базовый случай рекурсии
На этом работа рекурсии завершилась и итоговый список будет выглядеть таким
образом: [2, 3] + [5] + [10] = [2, 3, 5, 10]
```

**Сортировка слиянием**

```sh
def merge_sort(nums):
    if len(nums) > 1:
    mid = len(nums) // 2
    left = nums[:mid]
    right = nums[mid:]
    merge_sort(left)
    merge_sort(right)
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            nums[k] = left[i]
            i += 1
        else:
            nums[k] = right[j]
            j += 1
        k += 1

while i < len(left):
    nums[k] = left[i]
    i += 1
    k += 1

while j < len(right):
    nums[k] = right[j]
    j += 1
    k += 1
nums = [38, 27, 43, 3, 9, 82, 10]
merge_sort(nums)
print(nums)
```

## Функции высшего порядка, работа с файлами

```sh
def f(x)
    return x ** 2
g = f   # создали переменную типа “function” и положили в нее другую функцию
print(f(4)) # 16
print(g(4)) # 16

```

```sh
del calk(a, b):
    return a + b

def math(op, x, y): # передаем в аргумент функцию и 2 переменных
    print(op(x, y))

math(calk, 5, 45)
```

### Лямда функция

```sh
del calk(a, b):
    return a + b

calk = lambda a,b: a+b
sum(lambda a,b: a+b, 5, 45)


def math(op, x, y): 
    print(op(x, y))

math(lambda a,b: a+b, 5, 45)
```

*Задача. В списке хранятся числа. Нужно выбрать только чётные числа и составить список пар (число; квадрат числа).
Пример: 1 2 3 5 8 15 23 38
Получить: [(2, 4), (8, 64), (38, 1444)]*

```sh
data = [1, 2, 3, 5, 8, 15, 23, 38]
out = []
for i in data :
    if i % 2 == 0:
        out.append((i, i ** 2)) #t = () # создание пустого кортежа
print(out)

```

```sh
def select(f, col):
    return [f(x) for x in col]


def where(f, col):
    return [x for x in col if f(x)]

data = [1, 2, 3, 5, 8, 15, 23, 38]
res = select(int, data)

res = where(lambda x: x % 2 == 0, res)
print(res) # [2, 8, 38]

res = list(select(lambda x: (x, x ** 2), res))
```

### Функция map
Функция map() применяет указанную функцию к каждому элементу
итерируемого объекта и возвращает итератор с новыми объектами.

```sh
list_1 = [x for x in range (1,20)]
list_1 = list(map(lambda x: x + 10, list_1 ))
print(list_1)
```
*C клавиатуры вводится некий набор чисел, в качестве разделителя используется пробел. Этот набор чисел будет считан в качестве строки. Как превратить list строк в list чисел?*

```sh
data = list(map(int,input().split()))
```

### Функция .split()
преобразует строку('') в список ([])

```sh
st = '8 7 f     d'
print(st) # 8 7 f d

st = st.split()
print(st) # ['8', '7', 'f', 'd']

st = st.split(' ')
print(st)  # ['8', '7', 'f', '', '', '', '', 'd']

st = st.replace(" ",'-').split(' ') # метод replace перезапись пробелов на -
print(st) # ['8-7-f-----d']
```

### Функция filter
Функция filter() применяет указанную функцию к каждому элементу итерируемого объекта и возвращает итератор с теми объектами, для которых функция вернула True.

```sh
data = [x for x in range(10)]
res = list(filter(lambda x: x % 2 == 0, data)))
print(res) # [0, 2, 4, 6, 8]
```

### Функция zip
Функция zip() применяется к набору итерируемых объектов и
возвращает итератор с кортежами из элементов входных данных

```sh
users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]
data = list(zip(users, ids))
print(data) # [('user1', 4), ('user2', 5), ('user3', 9), ('user4', 14),
('user5', 7)]
```
Функция zip () пробегает по минимальному входящему набору:
```sh
users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]
salary = [111, 222, 333]
data = list(zip(users, ids, salary))
print(data) # [('user1', 4, 111), ('user2', 5, 222), ('user3', 333)]
```

### Функция enumerate
Функция enumerate() применяется к итерируемому объекту и
возвращает новый итератор с кортежами из индекса и элементов входных данных.

```sh
users = ['user1', 'user2', 'user3']
data = list(enumerate(users)
print(data) # [(0, 'user1'), (1, 'user2'), (2, 'user3))]
```

### Файлы

Варианты режима (мод):
1. **a – открытие для добавления данных.**

○ Позволяет дописывать что-то в имеющийся файл.

○ Если вы попробуете дописать что-то в несуществующий файл, то файл
будет создан и в него начнётся запись.

2. **r – открытие для чтения данных.**

○ Позволяет читать данные из файла.

○ Если вы попробуете считать данные из файла, которого не существует,
программа выдаст ошибку.

3. **w – открытие для записи данных.**

○ Позволяет записывать данные и создавать файл, если его не
существует.

Миксованные режимы:

4. **w+**

○ Позволяет открывать файл для записи и читать из него.

○ Если файла не существует, он будет создан.

**5. r+**

○ Позволяет открывать файл для чтения и дописывать в него.

○ Если файла не существует, программа выдаст ошибку

**Примеры** использования различных режимов в коде:

**1. Режим a**
```sh
colors = ['red', 'green', 'blue']
data = open('file.txt', 'a') # здесь указываем режим, в котором будем работать
data.writelines(colors) # разделителей не будет
data.close()
```
● data.close() — используется для закрытия файла, чтобы разорвать подключение файловой переменной с файлом на диске.

● exit() — позволяет не выполнять код, прописанный после этой команды в скрипте.

● В итоге создаётся текстовый файл с текстом внутри: redbluedreen.

● При повторном выполнении скрипта redbluedreenredbluedreen — добавление в существующий файл, а не перезапись файлов.
```sh
with open('file.txt', 'w') as data:
data.write('line 1\n')
data.write('line 2\n')
```
**2. Режим r**

● Чтение данных из файла:
```sh
path = 'file.txt'
data = open(path, 'r')
    for line in data:
print(line)
data.close()
```

**3. Режим w**
```sh
colors = ['red', 'green', 'blue']
data = open('file.txt', 'w')
data.writelines(colors) # разделителей не будет
data.close()
```
● В итоге создаётся текстовый файл с текстом внутри: ‘redbluedreen’.

● В случае перезаписи новые данные записываются, а старые удаляются.
