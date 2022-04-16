# Функции умеют не только принимать аргументы, необходимые для их выполнения,
# но и возвращать значения.
# Делается это с помощью ключевого слова return.
def pow_func(base, n=2):
   print(base ** n)

print(pow_func(3))
# 9
# None

# функции всегда что-то возвращают, и если этого не указали,
# то автоматически интерпретатор подставит строку return None в конец функции.
def pow_func(base, n=2):
   print(base ** n)
   return None

print(pow_func(3))

print('My Var')
def pow_func(base, n=2):
   print(base ** n)
   return (base ** n)

print(pow_func(3))

print('Skill Var')
def pow_func(base, n=2):
   inside_result = base ** n
   return inside_result


print(pow_func(3))