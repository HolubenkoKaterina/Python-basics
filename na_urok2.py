# Напишите программу, которая переворачивает строку задом наперед.
# def reverse(some_text):
#     some_text_new = some_text[::-1]
#     return some_text_new
# text = 'i like python'
# resalt = reverse(text)
# print(resalt)

# Определите, является ли строка палиндромом.
# def reverse(some_text):
#     if some_text == some_text[::-1]:
#         return True
#     else:
#         return False
# text = 'mamam1'
# resalt = reverse(text)
# print(resalt)

# Напишите функцию для удаления всех пробелов из строки.
# def reverse(some_text):
#     some_text_new = some_text.replace(' ', '')
#     return some_text_new
# text = 'i like python'
# resalt = reverse(text)
# print(resalt)

# Удалите все повторяющиеся символы из строки.
# text = 'i like Python python I love i'
#
# def delete_double_symbol(some_text: str):
#     lower_some_text = some_text.lower()
#
#     for elem in lower_some_text:
#
#         if lower_some_text.count(elem) > 1:
#             lower_some_text = lower_some_text.replace(elem, '')
#     return lower_some_text
# resalt = delete_double_symbol(text)
#print(resalt)

# Напишите функцию для объединения списка слов в строку с заданным разделителем.
# some_spisok = ['python', 'like', 'i', 'very', 'much']
# def join_to_str(some_text: list, divider):
#     some_string = ''
#     some_string = divider.join(some_text)
#     return some_string
# resalt = join_to_str(some_spisok, divider='! ')
# print(resalt)

# Удалите все символы, не являющиеся буквами и цифрами, из строки.
# text = ' 55h  !!! '
# def delete_symbols(some_text: str):
#     new_text = some_text.lower()
#     for elem in new_text:
#         if elem.isalnum():
#             new_text = new_text.replace(elem, '')
#     return new_text
# resalt = delete_symbols(text)
# print(resalt)

# Проверьте, состоит ли строка только из букв.
# text = ' 55h  !!! '
# def check_isalpha(some_text: str):
#     for elem in some_text:
#         if elem.isalpha():
#             return 'только буквы'
#         else:
#             return 'есть и буквы и цифры'
#
# resalt = check_isalpha(text)
# print(resalt)

# Проверьте, является ли строка числом.
# text = 'hgfd 789'
# def check_string(some_text: str):
#     for elem in some_text:
#         if elem.isnumeric():
#             return True
#         else:
#             return False
# resalt = check_string(text)
# print(resalt)

# Напишите функцию для замены всех символов в строке на их коды ASCII.
# text = 'hgfd 789!:%,'
# def change_code(some_text: str):
#     new_str = ""
#     for elem in some_text:
#         new_str += str(ord(elem)) + " "
#     return new_str
#
# resalt = change_code(text)
# print(resalt)

# Удалите все символы пунктуации из строки.
# import string
# text = 'hgfd 789!:%,'
# str_mark = '!%?,'
# new_text = text.maketrans('', '', str_mark)
# resalt = text.translate(new_text)

# def delete_punctuation(some_text: str):
#     for elem in some_text:
#         if elem.maketrans(!,:&?):
#             some_text = some_text.replace(elem)
#         return some_text
# resalt = delete_punctuation(text)
# print(resalt)
# Проверьте, является ли строка пустой.

# Напишите функцию для удаления определенной подстроки из строки.
# text = 'i like PYTHON so much python my LOVE'
# def del_substr(some_text: str, substr ):
#     new = some_text.lower().replace(substr, '', -1)
#     return new
# resalt = del_substr(text, substr='python')
# print(resalt)

# Удалите все пробелы и символы строки из начала и конца строки.
# text = '   i like PYTHON so much python my LOVE   '
# def delete_gaps(some_text: str):
#     new = some_text.strip()
#     return new
# resalt = delete_gaps(text)
# print(resalt)

# Подсчитайте количество слов в строке.
# text = 'i like PYTHON so much python my LOVE'
# for letters in text:
#     word = text.split()
#     resalt = len(word)
#     print(resalt)

# Проверить, состоит ли строка из одних только пробельных символов.
# text = ' j   '
# if text.isspace():
#     print(True)
# else:
#     print(False)
