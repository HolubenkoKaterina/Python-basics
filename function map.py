import requests
# Удвоить все числа в списке.
# list_my = ['14', 56, 100, ['14', 'spisok']]
# list_out = [int(elem) * 2 if type(elem) == int else elem for elem in list_my]
# print(list_out)

# Привести все строки к нижнему регистру.
# some_text = ['We Like PYTHON', 'WE LEARN HarD']
# list_out = [elem.lower() for elem in some_text if map(str, some_text)]
# print(list_out)

# Возвести все числа в квадрат.
# list_my = ['14', 56, 100, ['14', 'spisok']]
# list_out = [int(elem) ** 2 if type(elem) == int else elem for elem in list_my]
# print(list_out)
# list_out = list(map(lambda elem: elem ** 2 if type(elem) == int else elem, list_my))
# print(list_out)

# Умножить каждое число на 10.
# list_my = ['14', 56, 100, ['14', 'spisok']]
# list_out = list(map(lambda elem: elem * 10 if type(elem) == int else elem, list_my))
# print(list_out)

# Заменить все пробелы в строках на дефисы.
# some_text = ['We Like PYTHON', 'WE LEARN HarD']
# list_out = [elem.lower().replace(' ', '-') for elem in some_text if type(elem) == str  ]
# print(list_out)

# Увеличить все числа в списке на единицу.
# list_my = [5, 10, 15, 11, '11']
# list_out = [(elem + 1) if type(elem) == int else str(int(elem) + 1) if type(elem) == str and elem.isdigit()
#               else elem for elem in list_my]
# print(list_out)

# Отнимать 5 от каждого числа в списке.
# list_my = [5, 10, 15, 11, '11', 4]
# list_out = [elem - 5 if type(elem) == int  else elem for elem in list_my ]
# print(list_out)

# Преобразовать все элементы списка в абсолютные значения.
# list_my = [-5, 10, 15, 11, -112, 4]
# lisr_out = list(map(lambda elem: abs(elem), list_my))
# print(lisr_out)

# Перевести все элементы списка из градусов Цельсия в Фаренгейты.
# gradus = 18
# perevod = list(map(lambda gradus: gradus * 9/5 + 32, [gradus]))
# print(perevod)# тут сама не справилась, синтаксис.....ну и формула для перевода

# # Преобразовать все строки в списки слов.
# some_text = ['We Like PYTHON', 'WE LEARN HarD']
# list_out = list(map(lambda elem: elem.split(), some_text))
# print(list_out)
