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
b = 1
if a == b:
    a = a + 1
print(a, b)