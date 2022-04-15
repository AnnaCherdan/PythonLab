a = 1
b = 2
print(a > b) # а не больше b - вранье

# Проверка принадлежности
l = [1,2,3]
print(2 in l)
print(5 not in l)

# Проверка тождественности
a = 2
b = 3
print(a == b)
print(a is b)
print(a is not b)

# Условные операторы
a = 1
b = 6
if a == b:
    print('Ok')
else:
    print('Not ok')

a = 1
b = 2
if a == b:
    a = a + 1
print(a, b)
# З: Бьет ли конь, стоящий на клетке с координатами (номер строки и номер столбца) фигуру, стоящую на другой клетке.
# ВхД: вводятся 4 чисоа: координаты коня и координаты другой фигуры. Все координаты - целые числа в интервале 1 - 8.
# ВыхД: прога выводит слово YES, если конь может побить фигуру за 1 ход, иначе - NO.
# hx = int(input())
# hy = int(input())
# fx = int(input())
# fy = int(input())
#
# dx = abs(hx - fx)  # модуль расстояния по х.
# dy = abs(hy - fy)  # модуль расстояния по y
# # Надо проверить, что одна из этих разниц == 2, а вторая == 1.
# if dx == 2 and dy == 1:
#     print('YES')
# elif dx == 1 and dy == 2:
#     print('YES')
# else:
#     print('NO')

# Буквы и цифры в интервале от 1 до 8 и от A до H.

hx = input('Строка Коня: ')
hy = input('Столбец Коня: ')
fx = input('Строка Фигуры:')
fy = input('Столбец Фигуры:')

horse_x = ('1', '2', '3', '4', '5', '6', '7', '8')
horse_y = ('a', 'b', 'c', 'd', 'i', 'f', 'g', 'h')
figure_x = ('1', '2', '3', '4', '5', '6', '7', '8')
figure_y = ('a', 'b', 'c', 'd', 'i', 'f', 'g', 'h')

h_x = hx
h_y = hy
f_x = fx
f_y = fy

if hx in horse_x and hy in horse_y:
    print(f'Конь на клетке {h_y}{h_x}.')

if fx in figure_x and fy in figure_y:
    print(f'Фигура на клетке {f_y}{f_x}.')

hor_x = list(map(int, horse_x))
hor_y = list(map(int, horse_y))
print(hor_y)


# функцию hello_world, которая будет печать приветственную строку "Hello World".
# def hello_world():
#     m = 'hello, world'
#     print(m.replace('h', 'H').replace('w', 'W'))
#
#
# hello_world()

# a = int(input('Число 1: '))
# b = int(input('Число 2: '))
# print(max(a, b))
# print(max(a, b, 50))
# print(max([a, b]))
