# Прога выводит на экран числа от 1 до заданного клиентом, при этом вместо чисел, кратных 3, прога выводит слово "Bis",
# а вместо чисел, кратных пяти - слово "Taz". Если кратно обоим значениям - выводит "BisTaz"
# client = int(input('Введите число: '))
# for client in range(1, client + 1):
#     if client % 3 == 0 and client % 5 == 0:
#         print('BisTaz')
#     elif client % 3 == 0:
#         print('Bis')
#     elif client % 5 == 0:
#         print('Taz')
#     else:
#         print(client)
# # Пришла строка, нужно создать из нее список, состоящий из слов и посчитать длину каждого этого слова.
# l = input().split()  # split разобьет строку по пробелам. Если в скоюках
# # указать разделитель (":"), то разобьет по нему.
# print(l)
# for i in l:
#     print(i, len(i))
# print('Количество слов: ', len(l)) # Посчитали сколько слов в тексте.
# print('Количество пробелов: ', len(l) - 1) # Посчитали количетсво пробелов.
print('-' * 40)\

# #Список с числовыми значениями.
# # Посчитать сумму всех элементов в списке.
# l = input('').split()
# s = 0
# for i in l:
#     i = int(i) # Преобразование элемента списка в число.
#     s += i
#     print(s) # Если команда стоит внутри операции, то будет пошаговое выполнение!
print('-' * 20)

# ИЛИ
# l = input('').split()
# l = map(int, l) # Функция map преобразует в нужному типу данных.
# print(l)
# s = 0
# for i in l:
#     s += i
# print(s)
# # ИЛИ
print('-' * 20)

# l = input('').split()
# l = list(map(int, l)) # Функция map преобразует к нужному типу данных. Внешний список опять преобразует.
# print(l)
# s = 0
# for i in l:
#     s += i
# print(s)
print('-' * 20)

# ИЛИ
l = input('Введите цифры: ').split()
l = map(int, l) # Прописывает результат некрасиво. Лучше завернуть в list.
print(l)
# l - строка, а работать надо с цифрами. Чтобы не преобразовывать каждый элемент отдельно,
# используется map, т. е. она проходит внутри себя по каждому элементу списка и применяет
# к нему функцию int. Тип, к которому надо привести все элементы прописывается в скобках,
# затем - название списка.
print('-' * 20)

l = input('Введите цифры: ').split() # split разделил по пробелам, но все элементы в "". Убираем, завернцв в list.
print(l)
print(type(l[0]))
l = list(map(int, l))
print(type(l[0]))
print(l)
print('-' * 20)

# l2 = [4, 5, 6]
# print(l + l2)
#
# l = list(range(201)) # Функция range создаст список в диапазоне 0 - 200
# print(l)
# s = 0
# for i in l:
#     s += i
# print(s)
# print('-' * 20)

# l = [1, 2, 3] # Склеили списки.
# l2 = [4, 5, 6]
# print(l + l2)

# l = [1, 2, 3] # Склеили списки.
# l2 = [4, 5, 6]
# a =
# print(l + l2)
