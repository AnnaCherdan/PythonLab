# Вложенные условия.
# temp = int(input('Введите, пожалуйста, температуру на улице: '))
# if temp >= 15:
#         if temp >= 30:
#             print('В такую жару можно вообще не одеваться.')
#         else:
#             print('Жара. Допустимы майка и шорты.')
#     # print('Тепло, одевайтесь легко.')
# elif temp < -15:
#         if temp <= -30:
#             print('Дубак жуткий, сиди дома!')
#         else:
#             print('Холодно. Одевайтесь теплее.')
# else:
#     ...
print('-' * 20)
# Логические уcловия.
temp = int(input('Введите, пожалуйста, температуру на улице: '))
b = str(input('Какое у вас настроение? Плохое или хорошее: '))
g_mood =('Хорошее', 'Отличное')
if temp >= 15 and g_mood:
    print('Пора гулять!')
else:
    print('Лучше посидеть дома, поваляться, посмотреть фильмы, попить п...')

