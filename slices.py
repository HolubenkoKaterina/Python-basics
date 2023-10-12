# 1. Вывести первый символ строки.
# text = 'everything will be ok!'
# print(text[0])

# 2. Вывести последний символ строки.
# text = 'everything will be ok!'
# print(text[-1])

# 3. Вывести длину строки.
# text = 'everything will be ok!'
# print(len(text))

# 4. Вывести строку задом наперед.
# text = 'everything will be ok!'
# print(text[::-1])

# 5. Вывести первые 5 символов строки.
# text = 'everything will be ok!'
# print(text[:5])

# 6. Вывести последние 3 символа строки.
# text = 'everything will be ok!'
# print(text[-3::])

# 7. Вывести каждый третий символ строки.
# text = 'everything will be ok!'
# print(text[0::3])

# 8. Проверить, является ли строка палиндромом.
# text = 'everything will be ok!'
# text2 = 'mamam'
# if text2 == text2[::-1]:
#     print(True)
# else:
#     print(False)

# 9. Посчитать количество символов в строке.
# text = 'everything will be ok! Fre you ok?'
# print(len(text))

# 10. Посчитать количество определенного символа в строке.
# text = 'everything will be OK! Fre you ok?'
# def counter_symbol(some_text: str, symbol):
#     counter = 0
#     for letter in text.lower():
#         if letter == symbol:
#             counter += 1
#     return counter
# resalt = counter_symbol(text, symbol='o')
# print(resalt)

# 11. Заменить все пробелы в строке на дефисы.
# text = 'everything will be OK! Fre you ok?'
# def replace_symbol(some_text: str):
#     some_text = some_text.replace(' ', '-')
#     return some_text
# resalt = replace_symbol(text)
# print(resalt)

# 12. Проверить, начинается ли строка с определенного префикса.
# pref = 'fever'.lower()
# text = 'everything will be OK! Fre you ok?'.lower()
# if text.startswith(pref):
#     print(True)
# else:
#     print(False)

# 13. Проверить, заканчивается ли строка определенным суффиксом.
# suf = 'fever'.lower()
# text = 'everything will be OK! Fre you ok?'.lower()
# if text.endswith(suf):
#     print(True)
# else:
#     print(False)

# 14. Сравнить две строки на равенство.
# text = 'everything will be ok!'
# text2 = 'mamam'
# if text == text2:
#     print('+')
# else:
#     print('-')

# 15. Преобразовать строку в верхний регистр.
# cc
# print(text.upper())

# 16. Преобразовать строку в нижний регистр.
# text = 'EVERYTHING WILL BE OK!'
# print(text.lower())

# 17. Удалить все пробелы из строки.
# text = 'everything will be ok!'
# new = ''.join(text.split())
# print(new)

# 19. Объединить две строки в одну.
# text = 'everything will be ok!'
# text1 = 'EVERYTHING WILL BE OK!'
# print(text + text1)

# 20. Проверить, содержит ли строка только буквы.
# text = 'everything will be ok!'
# print(text.isalpha())

# 21. Проверить, содержит ли строка только цифры.
# text = 'everything will be ok!'
# print(text.isnumeric())

# # 22. Проверить, содержит ли строка буквы и цифры.
# text = 'everything will be ok!'
# print(text.isalnum())

# 23. Разделить строку на список слов.
# text = 'everything will be ok!'
# out = []
# for words in text.split():
#     out.append(words)
# print(out)

# 24. Проверить, все ли символы в строке являются буквами.
# text = 'everything will be ok!'
# print(text.isalpha())

# 25. Проверить, все ли символы в строке являются цифрами.
# text = 'everything will be ok!'
# print(text.isalnum())

# 26. Найти индекс первого вхождения подстроки в строку.
# my_string = "Hello, world! Hello, Python!"
# substring = "Hello"
# first_index = my_string.find(substring)
# if first_index != 1:
#     print(f"Подстрока '{substring}' найдена на позиции {first_index}")
# else:
#     print(f"Подстрока '{substring}' не найдена в строке.")

# 27. Найти индекс последнего вхождения подстроки в строку.
# my_string = "Hello, world! Hello, Python!"
# substring = "Hello"
# last_index = my_string.rfind(substring)
# if last_index != -1:
#     print(f"Подстрока '{substring}' найдена на позиции {last_index}")
# else:
#     print(f"Подстрока '{substring}' не найдена в строке.")

# 28. Заменить все вхождения подстроки в строке на другую строку.
# text = 'everything will be ok!'
# substr = 'er'
# if substr in text.lower():
#     text = text.replace(substr, substr.upper())
# print(text)

# 29. Перевернуть каждое слово в строке задом наперед.
# text = 'everything will be ok!'
# for words in text.split():
#     print(words[::-1])

# 30. Проверить, является ли строка числом.
# text = 'everything will be ok!'
# print(text.isnumeric())

# 31. Сгенерировать новую строку, повторив исходную заданное количество раз.
# text = 'everything will be ok!'
# print(text * 3)

# 32. Извлечь числа из строки и сложить их.
# text = 'everything will be ok! 52, 46, 58'
# for elem in text.split():
#     summa = 0
#     if elem.isdigit():
#         summa += int(elem)
# print(summa)

# 33. Разбить строку на две строки по середине.
# text = 'everything will be ok!'
# substr = len(text) // 2
# new = text[:substr]
# new2 = text[substr:]
# print(new)
# print(new2)

# 34. Проверить, содержит ли строка только буквы верхнего регистра.
# text = 'everything will be Ok! 52, 46, 58'
# print(text.isupper())

# 35. Проверить, содержит ли строка только буквы нижнего регистра.
# text = 'everything will be ok! 52, 46, 58'
# print(text.islower())

# 36. Заменить все гласные буквы в строке на звездочки (*).
# my_string = 'Everything will be OK! '
# for letter in my_string:
#     if letter in 'aeouiAEIOU':
#         my_string = my_string.replace(letter, '*')
# print(my_string)

# 37. Подсчитать количество гласных букв в строке.
# text = 'everything will be Ok! 52, 46, 58'.lower()
# vowels = 'aeuoiy'
# counter = 0
# for letter in text:
#     if letter.isalpha() and letter  not in vowels:
#         counter += 1
# print(counter)

# 38. Подсчитать количество согласных букв в строке.
# text = 'everything will be Ok! 52, 46, 58'.lower()
# vowels = 'aeuoiy'
# counter = 0
# for letter in text:
#     if letter.isalpha() and letter in vowels:
#         counter += 1
# print(counter)

# 39. Проверить, все ли слова в строке начинаются с большой буквы.
# my_string = 'Everything will be OK! '
# if my_string.istitle():
#     print('+')
# else:
#     print('-')

# 40. Удалить лишние пробелы между словами в строке.
# my_string = ' everything will be OK! '
# print(my_string)
# my_string = my_string.strip()
# print(my_string)
