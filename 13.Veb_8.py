# enumirate, zip
l = ['a', 'b', 'c']
for elem in l:
    print(elem) # Поочередно пропишет элементы и список
    print(l)    # Поочередно пропишет элементы и список
print(elem)     # Пропишет последний элемент списка.
print(l)        # Пропишет список.

l = ['a', 'b', 'c']
for index, elem in enumerate(l):    # Для работы с индексами элементов списка.
    print(index)
    print(elem)
#     ИЛИ
for index in range(len(l)):
    elem = l[index]
    print(index)
    print(elem)

l = ['a', 'b', 'c']
l2 = [' - первая буква', ' - вторая буква', ' - третья буква']
for index in range(len(l)):
    elem1 = l[index]
    elem2 = l2[index]
    print(elem1, elem2)

#     ИЛИ
l = ['a', 'b', 'c']
l2 = [' - первая буква', ' - вторая буква', ' - третья буква']
for elem1, elem2 in zip(l, l2):
    print(elem1, elem2)

# break, continue

# a = 10
# n = 10
# for i in range(1, n):
#     a += i
#     if a > 30:
#         break
#     print(a)
# print(a)
#
# a = 10
# k = 3
# for i in range(1,n):
#     a += k
#     print(a)

a = 10
n = 10
k = 3
for i in range(1, n):
    a += k
    if a % 2 != 0:  # только четные. 10+3, 13+3, 16+3 и т.д.
        continue
    print(a)

# Списковое включение.

a = [i for i in range(10)]
print(a)
a = [i**2 for i in range(10)]
print(a)

# По данному действительному числу а и нитуральному n вычеслить сумму 1 + а + а**2...a**n.
# ВхД: вводятся 2 числа а и n.
# ВыхД: выводится сумма.

a = int(input('Число а: '))
n = int(input('Число n: '))

s = 0  # Изначально сумма равна 0.
for i in range(n + 1):   # Перебираем переменную i со степенью от 0 до n.
    s += a ** n
    print()

