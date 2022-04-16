# Прога возвращает количество делителей числа a. На сколько чисел можно поделить делимое в диапазоне.
print('Skill Var')
def get_multipliers(a):
    count = 0
    for n in range(1, a + 1): # Чтобы указанное в скобках число-аргумент входило в диапазон + 1.
        if a % n == 0:
            count += 1

    return count
print(get_multipliers(16)) # 16 делится без отстатка на: 1, 2, 4, 8, 16.
print(get_multipliers(4)) # 4 делится без отстатка на: 1, 2, 4.
print(get_multipliers(6)) # 6 делится без отстатка на: 1, 2, 3, 6.
print(get_multipliers(17)) # 17 делится без отстатка на: 1, 17.