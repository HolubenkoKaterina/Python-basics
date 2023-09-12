# Определить длину строки.
# def lenght_str(some_str):
#     return len(some_str)
# resalt = lenght_str('i like python')
# print(resalt)

# Сделать строку заглавной (в верхнем регистре).
# stroka = 'i like python so much!'
# def stroka_upper(some_text:str):
#     return some_text.upper()
# resalt = stroka_upper(stroka)
# print(resalt)

# Сделать строку строчной (в нижнем регистре).
# text = 'I LIKE PYTHON SO MUCH!'
# def stroka_lower(some_text):
#     return some_text.lower()
# resalt = stroka_lower(text)
# print(resalt)

# Подсчитать количество определенного символа в строке.
# def counter_symbol(text, symbol):
#     counter = 0
#     for letters in text.lower():
#         if letters == symbol:
#             counter += 1
#     return f'{counter} кол-во символов'
# text = 'I LIKE PYTHON SO MUCH!'
# resalt = counter_symbol( text, symbol='e')
# print(resalt)

# Проверить, является ли строка палиндромом.
#text = 'I LIKE PYTHON SO MUCH!'
# text_2 = 'Atata'
# def check_string_pаlindrom(some_text: str):
#     if some_text.lower() == some_text[::-1].lower():
#         return f'строка {some_text}  является палиндромом'
#     else:
#         return f'строка {some_text}  не является палиндромом'
# resalt = check_string_pаlindrom(text_2)
# print(resalt)

# Обрезать пробельные символы в начале и конце строки.
# text = '  I LIKE PYTHON SO MUCH!   '
# def delete_gap(some_text: str):

# Заменить подстроку в строке на другую подстроку.
# text = 'I LIKE PYTHON SO MUCH!'.lower()
# find_change_substr = 'very'
# to_change_substr = 'so'
# def change_substr(some_text):
#
#     if to_change_substr.lower() in some_text.lower():
#         new_text = some_text.replace(to_change_substr, find_change_substr)
#         return new_text
#     else:
#         raise ValueError('подстрока не найдена')
# resalt = change_substr(text)
# print(resalt)

# Разделить строку на подстроки по заданному разделителю.
# text = 'I LIKE PYTHON SO MUCH!'.lower()
# def do_substr(some_text: str, divider):
#     if divider in some_text:
#         new_text = some_text.split(divider)
#         return new_text
# resalt = do_substr(text, divider='e')
# print(resalt)