# Функция — это блок кода, который начинается с ключевого слова def, затем следует название
# функции, затем скобки, в которых указываются аргументы функции, и двоеточие в конце.
# Со следующей строки начинается тело функции. Это именно тот участок, который будет
# выполняться при вызове функции.
# def name_func():
#     # начало тела функции
#     ...
#     # конец тела функции

def char_frequency():
   text = """
   У лукоморья дуб зелёный;
   Златая цепь на дубе том:
   И днём и ночью кот учёный
   Всё ходит по цепи кругом;
   Идёт направо -- песнь заводит,
   Налево -- сказку говорит.
   Там чудеса: там леший бродит,
   Русалка на ветвях сидит;
   Там на неведомых дорожках
   Следы невиданных зверей;
   Избушка там на курьих ножках
   Стоит без окон, без дверей;
   Там лес и дол видений полны;
   Там о заре прихлынут волны
   На брег песчаный и пустой,
   И тридцать витязей прекрасных
   Чредой из вод выходят ясных,
   И с ними дядька их морской;
   Там королевич мимоходом
   Пленяет грозного царя;
   Там в облаках перед народом
   Через леса, через моря
   Колдун несёт богатыря;
   В темнице там царевна тужит,
   А бурый волк ей верно служит;
   Там ступа с Бабою Ягой
   Идёт, бредёт сама собой,
   Там царь Кащей над златом чахнет;
   Там русский дух... там Русью пахнет!
   И там я был, и мёд я пил;
   У моря видел дуб зелёный;
   Под ним сидел, и кот учёный
   Свои мне сказки говорил.
   """

   text = text.lower()
   text = text.replace(" ", "")
   text = text.replace("\n", "")

   count = {}  # для подсчета символов и их количества
   for char in text:
       if char in count:  # если символ уже встречался, то увеличиваем его количество на 1
           count[char] += 1
       else:
           count[char] = 1

   for char, cnt in count.items():
       print(f"Символ {char} встречается {cnt} раз")

...

# вызвали функцию в любом месте программы
char_frequency()
print('-' * 20)

def print_2_add_2(): # My var
    a = 2
    b = 2
    c = a + b
    print(2 + 2)
    print(c)


print_2_add_2()


def print_2_add_2(): # Skill var
     result = 2 + 2
     print(result)


print_2_add_2()
print('-' * 20)

