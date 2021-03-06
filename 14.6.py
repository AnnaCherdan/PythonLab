# Вот псевдокод, по которому работает map.
# Псевдокод — компактный, зачастую неформальный, способ описания алгоритмов,
# использующий ключевые слова языков программирования, но опускающий несущественные для понимания алгоритма
# подробности и специфический синтаксис.
def map_(func, some_list):
    # some_list объект, над которым будет производиться преобразование
    # func функция, которая должна выполняться над каждым объектом
    outp = []
    for i in range(len(some_list)):
        outp.append(func(some_list[i]))
    return outp
# Чтобы не использовать такую конструкцию каждый раз, введена встроенная функция:
#
# map(function, iter1, iter2, ...)
# iter1, iter2, ... — может быть 1 и более итерируемых объектов, однако на вход
# функции должно приходить такое же количество аргументов.
# function — ссылка на функцию.

# print(list(map(pow_, a_list)))  # [1, 4, 9]
#
# for i in map(pow_, a_list):
#    pass

L = ['THIS', 'IS', 'LOWER', 'STRING']
# print(L.lower) BAD Var

print(list(map(str.lower, L)))

# Функция filter согласно своему названию фильтрует элементы итерируемого объекта.
#
# Она принимает на вход:
#
#         функцию, которая должна возвращать bool значение (True или False);
#         итерируемый объект, над которым будет производиться фильтрация (в этом случае можно передать только один объект).
#
# Функция filter возвращает итератор с теми элементами из входящей последовательности, для которых функция вернула True.
#
# Псевдокод:
#
def filter(func, cont):
    outp = []
    for x in cont: # проходим циклом по итерируемому объекту
        if func(x): # проверяем условие для каждого элемента
            outp.append(x) # если True, добавляем в новый список
    return outp


# Из заданного списка вывести только положительные элементы
def positive(x):
    return x > 0  # функция возвращает только True или False

result = filter(positive, [-2, -1, 0, 1, -3, 2, -3])

# Возвращается итератор, т.е. перечисляйте или приводите к списку
print(list(result))   # [1, 2]

def positive(x):
    return x % 2 == 0

result = filter(positive, [-2, -1, 0, 1, -3, 2, -3])

print(list(result))



# map + filter
some_list = [i - 10 for i in range(20)]
def pow2(x): return x**2
def positive(x): return x > 0

print(some_list)
print(list(map(pow2, filter(positive, some_list))))

# Тоже самое через list comprehension:

# [i**2 for i in some_list if i > 0]

# map работает по принципу ленивых вычислений, а list comprehension возвращает результат вычислений сразу.
#
# map(func, list1)  # итератор, но никаких вычислений не будет произведено
# list(map(...))  # только здесь появляется объект
#
# [func(i) for i in list1]  # сразу готовый объект
#
#
# [func(i) for i in list1] == list(map(func, list1))  # результат один и тот же

# анонимные функции. Объявляются они по ключевому слову lambda.
#
# # эти две функции выполняют одно и тоже — складывают два числа
# def my_function(x1, x2):  # Обычная функция
#    return x2 + x1
#
# lambda x1, x2: x2 + x1  # Анонимная функция
#
# Анонимные функции могут содержать в себе только одну инструкцию (выражение), которую они выполняют.
#
# # Возвести первые 10 натуральных чисел в квадрат
# list(map(lambda x: x ** 2, range(1, 11)))  # правильно
# # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#
# list(map(lambda x: x ** 2; x + 1, range(1, 11)))  #  неправильно, так как lambda содержит две конструкции
# словарь сортируется по ключам.
#
d = {2 : "c", 1 : "d", 4 : "a", 3 : "b"}
#
# # Чтобы отсортировать его по ключам, нужно сделать так:
print(dict(sorted(d.items())))
# # {1: 'd', 2: 'c', 3: 'b', 4: 'a'}
#
# А вот чтобы отсортировать словарь по значениям, необходимо указать, что сортировать нужно по второму элементу кортежа ключ-значение. Тут на помощь приходят lambda-функции. У встроенной функции sortred() можно задать аргумент key, который укажет, по какому ключу нужно производить сортировку.
#
sorted(d.items(), key=lambda x: x[1])  # сортировка по значению словаря

# список с данными о росте и весе людей. Задача — отсортировать их по индексу массы тела.
# Он вычисляется по формуле: рост в метрах возвести в квадрат, потом массу тела в килограммах
# разделить на полученную цифру.

# (вес, рост)
data = [
   (82, 191),
   (68, 174),
   (90, 189),
   (73, 179),
   (76, 184)
]


sorted(data, key = lambda x: x[0] / x[1] ** 2)



