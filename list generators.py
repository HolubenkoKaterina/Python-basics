# Создайте лямбда-функцию, которая возвращает список строк в обратном порядке.
# some_text = ['i like python', 'we can learn']
# print(some_text[::-1])

# Создать список всех возможных комбинаций букв "ABC" и цифр "123" с использованием генератора списков
import itertools
# list1 = "ABC"
# list2  = "123"
# list_out = [(elem, element) for elem in list1 for element in list2] + [(element, elem) for elem in list1 for element in list2 ]
# print(list_out)

# Создать список всех факториалов чисел от 1 до 10 с использованием генератора списков.
# def factorial(number: int):
#     resalt = 1
#     for num in range(1, number +1):
#         resalt *= num
#     return resalt
# resalt = factorial(5)
# list_out = [factorial(elem) for elem in range(1, 11)]
# print(list_out)

# Создайте лямбда-функцию, которая возвращает список строк, в которых каждая буква заменена на её номер в алфавите
# (например, "a" становится 1, "b" становится 2 и т.д.).
# text = "Hello, World!"
# list_out = lambda text: [str(ord(letter.lower()) - 96) for letter in text if letter.isalpha()]
# print(list_out(text)) # то очень сложно, прям печалька)

#Извлечь из списка только строки, состоящие из заглавных букв.
# some_spisok = ['We', 'like',  'Python', 'we', 'did', 'it', 'hello', 'morning', 'sidr']
# def get_strings_upper_letter(args):
#     list_out = [element for element in args if element.isupper()]
#     return list_out
#
# result = get_strings_upper_letter(some_spisok)
# print(result)
