# Введите с клавиатуры номер месяца. Определите сезон в зависимости от номера месяца и выведите сообщение:
#
#         «Весна» для 3, 4, 5 месяца;
#         «Лето» для 6, 7, 8 месяца;
#         «Осень» для 9, 10, 11 месяца;
#         «Зима» для 12, 1, 2 месяца.
# хорошо
# month in [3, 4, 5]
#
# # плохо
# month == 3 or month == 4 or month == 5

# НАДО ТАК
# month = int(input(
#
# if month in [3, 4, 5]:
#     print("Весна")
# elif month in [6, 7, 8]:
#     print("Лето")
# elif month in [9, 10, 11]:
#     print("Осень")
# elif month in [12, 1, 2]:
#     print("Зима")

#  есть заготовка — def get_wind_class(speed):, давайте разберёмся с ней:
#
#         инструкция def говорит нам о том, что мы объявляем функцию;
#         get_wind_class — имя нашей функции;
#         speed — переменная, которую мы передаём в функцию (а она уже с ней что-то делает).

# слово return вместо print. Ключевое слово return возвращает значение, которое идет после него.

# У вас есть заготовка функции — def get_wind_class(speed):
# Вам нужно вместо "???" написать цикл, который возвращает из функции класс ветра в зависимости от его характера:
# от 1 до 4 м/с - "weak [1]"
# от 5-10 м/c - "moderate [2]"
# от 11-18 м/c - "strong [3]"
# от 19 м/c - "hurricane [4]"

# def get_wind_class(speed): #объявление функции
#     if 1 <= speed <= 4: #только аргумент
#         return "weak [1]"
#     elif 5 <= speed <= 10:
#         return "moderate [2]"
#     elif 11 <= speed <= 18:
#         return"strong [3]"
#     elif speed >= 19:
#         return "hurricane [4]"
# print(get_wind_class(3)) #мы просим программу напечатать то, что в скобках

# Допишите функцию check_user так, чтобы она по логину пользователя
# проверяла, существует он или нет,
# после чего с помощью вложенного условия проверяла
# правильность пароля этого пользователя.
# Функция должна возвращать только True или False.
# Чтобы вернуть True, напишите "return True";
# чтобы вернуть False, напишите "return False".

# user_database = {
#     'user': 'password',
#     'iseedeadpeople': 'greedisgood',
#     'hesoyam': 'tgm'
# }
# def check_user(username, password):
#     if username in user_database:
#         if password == user_database[username]:
#             return True
#         else:
#             return False
#     else:
#         return False

a = 42
b = 45

if a > b:
    result = a
else:
    result = b
result = a if a > b else b # тернарный условный оператор или инлайновый if
print(result)

# Запишите условие, которое является истинным, когда только одно из чисел А, В и С
# меньше 45. Иногда проще записать все условия и не пытаться упростить их.

# A = int(input('Введите первое число\n'))
# B = int(input('Введите второе число\n'))
# C = int(input('Введите третье число\n'))
#
# if ((A < 45) and (B >= 45) and (C >=45)) or \
#     ((A >= 45) and (B < 45) and (C >=45)) or \
#     ((A >= 45) and (B >= 45) and (C < 45)):
#     print('Есть число меньше 45 и только одно')
# else:
#     print('Числа меньше 45 нет или их несколько')


# Запишите логическое выражение, которое определяет,
# что число А не принадлежит интервалу от -10 до -1 или интервалу от 2 до 15.

# A = int(input('Введите число\n'))
# #
# # if not (-10 <= A <= -1 or 2 <= A <= 15):
# #     print("Число не принадлежит интервалу")
# # else:
# #     print("Число принадлежит интервалу")

# Дано двузначное число. Определите, входит ли в него цифра 5. Попробуйте решить задачу с
# использованием целочисленного деления и деления с остатком.
n = 15
first_digit = n // 10
second_digit = n % 10

print((first_digit == 5) or (second_digit == 5))

# Проверьте, все ли элементы в списке являются уникальными.
list_ = [-5, 2, 4, 8, 12, -7, 5]

print(len(list_) == len(set(list_)))

# Дано натуральное восьмизначное число.
# Выясните, является ли оно палиндромом (читается одинаково слева направо и справа налево).

num = 12345678

print(str(num) == str(num)[::-1])