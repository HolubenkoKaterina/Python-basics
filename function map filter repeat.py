# Преобразовать каждый элемент списка строк в список слов, разделенных пробелами.
# my_strings = ['apple', 'banana', 'cherry', 'date']
# list_out = list(map(str.split, my_strings))
# print(list_out)
# list_out = []
# for elem in my_strings:
#     words = elem.split()
#     list_out.append(words)
# print(list_out)

# Отфильтровать список строк, оставив только строки длиной больше 5 символов.
# my_strings = ['apple', 'banana', 'cherry', 'date']
# resalt = list(filter(lambda elem: len(elem) > 5, my_strings))
# print(resalt)

# # Преобразовать каждый элемент списка в строку и добавить к нему префикс "Item: ".
# my_strings = ['1', '4', '8', '10']
# resalt = list(map(str, my_strings))
# itog = ["Item: " + elem for elem in resalt]
# print(itog)

# Отфильтровать список чисел, оставив только четные числа.
# import random
# list_numb = list(range(random.randint(14, 75)))
# print(list_numb)
# resalt = list(filter(lambda elem: elem % 2 == 0, list_numb))
# print(resalt)

# Вычислить сумму цифр в каждом элементе списка чисел.
# import random
# list_numb = random.sample(range(15, 26), random.randint(1, 13))
# #последовательность чисел от 15 до 25, длина списка будет варьироватся от 1 до 12
# print(list_numb)
# list_out = []
#
# for num in list_numb:
#     summa = 0
#     for digit in str(num):
#         summa += int(digit)
#     list_out.append(summa)
#
# print(list_out)

# Преобразовать каждый элемент списка в его абсолютное значение.
# import random
# list_numb = random.sample(range(-10, 26), random.randint(1, 13))
# print(list_numb)
# resalt = list(abs(elem) for elem in list_numb)
# print(resalt)

# Удвоить каждую букву в каждом элементе списка строк.
# my_strings = ['apple', 'banana', 'cherry', 'date']
# list_out = []
# for words in my_strings:
#     new_words = ''
#     for letter in words:
#         if not letter.isdigit():
#             new_words += letter * 2
#     list_out.append(new_words)
# print(list_out)
# list_out = [''.join(letter * 2 for letter in word if not letter.isdigit()) for word in my_strings]

# Отфильтровать список строк, оставив только строки, содержащие букву 'a'.
# my_strings = ['apple', 'banana', 'cherry', 'date']
# list_out = list(filter(lambda  elem: 'a' in elem, my_strings))
# print(list_out)

# Преобразовать каждый элемент списка строк в список букв.
# my_strings = ['apple', 'banana', 'cherry', 'date']
# list_letter_of_elem = []
# for elem in my_strings:
#     words = [letter for letter in elem]
#     print(words)

# Отфильтровать список чисел, оставив только числа, большие 10.
# import random
# list_numbers = list(random.sample(range(5, 40), random.randint(10, 15)))
# print(list_numbers)
# list_out = list(filter(lambda elem: elem > 10, list_numbers))
# print(list_out)

# # Умножить каждый элемент списка на его индекс.
# import random
# list_numbers = list(random.sample(range(5, 40), random.randint(10, 15)))
# list_out = [elem * index for index, elem in enumerate(list_numbers)]
# print(list_out)

# # Отфильтровать список строк, оставив только палиндромы.
# list_strings = ["radar and level", "A man, a plan, a canal: Panama",  "Was it a car or a cat I saw?",
#                  "Evil is a name of a foeman, as I live.", 'lisa', 'miska']
# list_out = []
# for elem in list_strings:
#     clean_elem = elem.lower().split()
#     if clean_elem != clean_elem[::-1]:
#         list_out.append(elem)
# print(list_out)

# Преобразовать список имен в список инициалов (например, "John Smith" в "J. S.").
# names = ["John Smith", "Jane Doe", "Michael Johnson"]
# initials = []
# for name in names:
#     parts = name.split()
#     first_initial = parts[0][0].upper()
#     last_initial = parts[1][0].upper()
#     full_initials = f"{first_initial}. {last_initial}."
#     initials.append(full_initials)
# print(initials)

# Отфильтровать список чисел, оставив только числа, оканчивающиеся на 5.
# import random
# list_nums = random.sample(range(5, 45), random.randint(5, 15))
# print(list_nums)
# list_out = list(filter(lambda elem: str(elem).endswith('5'), list_nums))
# print(list_out)

# Преобразовать каждый элемент списка строк в список их гласных букв.
# vowels = 'aeouyi'
# my_list = ['apple', 'banana', 'cherry', 'date']
# list_out = []
# for elem in my_list:
#     list_vowels = [letter for letter in elem if letter.lower() in vowels]
#     list_out.append(list_vowels)
#
# print(list_out)

# Отфильтровать список строк, оставив только строки, содержащие только буквы.
# list_strings = ["apple", "42", "banana", "7", "cherry", "16", "date"]
# list_out = list(filter(lambda elem: not elem.isdigit(), list_strings))
# print(list_out)

# Преобразовать список списков в список их длин.
# list_out1 = []
# my_lists = [[1, 2, 3, 8], [4, 5], [7, 8, 9]]
# for elem in my_lists:
#     list_out.append(len(elem))
# print(list_out)
# list_out = list(map(len, my_lists))

