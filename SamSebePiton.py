# m = input('Как Вас зовут?: ')
# print("Привет, " + m)
#
# nastroy = input('Как настроение?: ')
# bad_nast = ['плохо', "Плохо", "хреново", "Хренова", "плохое"]
# godd_nast = ['хорошо', "Хорошо", "отлично", "Отлично", "хорошее"]
# if nastroy in bad_nast:
#     print('Как я тебя понимаю. Но поверь, все будет отлично!')
# elif nastroy in godd_nast:
#     print('Замечательно! Рада за тебя!')
# else:
#     print('Загадки загадываем? Давай еще раз...')

a = 1; b = 2; print(a, b) # Так делать не надо.
# # a = 1, b = 2, print(a, b) # BAD Var не может быть назначен литералу

# nastroy = input('Как настроение?: ')
# bad_nast = ['плохо', "Плохо", "хреново", "Хренова", "плохое"]
# good_nast = ['хорошо', "Хорошо", "отлично", "Отлично", "хорошее"]
# if nastroy in bad_nast:
#     print('Как я тебя понимаю. Но поверь, все будет отлично!')
# elif nastroy in good_nast:
#     print('Замечательно! Рада за тебя!')
# elif nastroy in bad_nast or good_nast:
#     print('Эк тебя колбасит...')
# else:
#     print('Загадки загадываем? Давай еще раз...')

# Допустимо записывать одну инструкцию в нескольких строках. Достаточно ее за-
# # ключить в пару круглых, квадратных или фигурных скобок:
a = 1
b = 2
c = 3
v = 4
gu = [a, b, c, v]
if (a or b or c or v <= 5):
    print('Оно меньше 5.')
# for i in gu:

# Тело составной инструкции может располагаться в той же строке, что и тело основ-
# ной, если тело составной инструкции не содержит составных инструкций.
if a > b:
    print('Враньё')
else:
    print("Правда")

# Комплексные числа записываются с «j» как мнимой частью:

x = 3+5j
y = 5j
z = -5j
print(x)
print(type(y))
print(type(z))

# Оператор принадлежности подстроки in. Есть также оператор not in, у которого обратная логика.
# Оператор in возвращает True, если подстрока входит в строку, и False, если нет

# a = input('Введи что-нибудь: ')
# z = 'l'
# print('l' in a)
# print(z not in a)

# chr()	Преобразует целое число в символ для ASCII и Unicode
s = chr(123)
print(s)

# ord()	Преобразует символ в целое число для ASCII и Unicode
print(ord('k'))

# len()	Возвращает длину строки
print(len('jhjdksjdfjk kdjfdjsdhjf'))

# str()	Изменяет тип объекта на string
a = 25
c = str(25)
print(c)
print(type(c))
b = str(6655)
print(b)
print(type(b))
print(str(565))


# Индексация строк.  Доступ к отдельным символам в строке можно получить,
# указав имя строки, за которым следует число в квадратных скобках [].

s = 'Привет, мартышка!'
print(s[14])
print(s[5], s[16])
print(len(s))

s = ['fdf', 'oit', 'oio']

print(len(str(s)))
print(s[0])
print(s[1])
print(s[-1])

# Срезы строк. Если s это строка, выражение формы
# s[m:n] возвращает часть s, начинающуюся с позиции m, и до позиции n, но не включая позицию

# Есть список a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89].
# Выведите все элементы, которые меньше 5.
print('My GOOD VAR')
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for i in a:
    if i < 5:
        print(i, end=',')
    else:
        ...


print('Other VAR')
print(list(filter(lambda elem: elem < 5, a)))  # воспользоваться функцией filter,
                                               # которая фильтрует элементы согласно заданному условию.
print('MOST GOOD VAR')
print([elem for elem in a if elem < 5])


# Даны списки:
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# Нужно вернуть список, который состоит из элементов, общих для этих двух списков.
print('My BAD VAR') # Склеила списки, но оставила все элементы, только убрав дубликаты.
c = a + b
print(list(set(c)))

print('Other VAR')
result = list(filter(lambda elem: elem in b, a))
print(result)

# ИЛИ списковым включением:
result = [elem for elem in a if elem in b]
print(result)

# привести оба списка к множествам и найти их пересечение:
result = list(set(a) & set(b))
print(result)

# Отсортируйте словарь по значению в порядке возрастания и убывания.

# a = {'b':'1', 'c':'2', 'd':'3', 'f':'4'}
# print(sorted(values))









