# Создайте список чисел и получите его итератор.
# numbers = range(0, 15)
# numbers_iterator = iter(numbers)
# print(next(numbers_iterator))
# print(next(numbers_iterator))

# Используйте итератор для получения следующего элемента списка.
# number = iter(range(4, 9))
# print(next(number))

# Создайте словарь итератора, где ключами будут числа от 1 до N, а значениями - соответствующие итераторы.
# def some_dict(n: int):
#     iterators_dict = {num: iter(range(num)) for num in range(1, n+1)}
#     return iterators_dict
# resalt = some_dict(5)
# print(resalt)
#
# Создайте список из квадратов чисел от 1 до 10 с помощью выражения-генератора.
# list_out = (num ** 2 for num in range(1, 10))
# print(list_out)

# Создайте множество из первых 10 четных чисел с помощью выражения-генератора.
# n = 14
# some_set = {num for num in range(1, (n * 2) + 1) if num % 2 == 0}
# print(some_set)
#
# Создайте множество из квадратов чисел от 1 до 10 с помощью set comprehension.
# some_resalt = {num ** 2 for num in range(1, 11)}
# print(some_resalt)

# Создайте множество из первых 10 четных чисел с помощью set comprehension.
# n = 10
# some_set = {num ** 2 for num in range(1, (n*2)+1 )}
# print(some_set)

# Создайте словарь, где ключами будут числа от 1 до 10, а значениями - их квадраты, с помощью dictionary comprehension.
# some_dict = {key: key ** 2 for  key in range(1, 11)}
# print(some_dict)

# Создайте словарь, где ключами будут буквы из слова "привет", а значениями - их позиции в слове, с помощью dictionary comprehension.
# text = 'helloo'
# some_dict = {letter: index for index, letter, in enumerate(text)}
# print(some_dict)

# Создайте строку и получите ее итератор с помощью iter().
# Используйте next() для получения следующего символа строки с помощью итератора.
# text = 'we like python'
# iterator = iter(text)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

# Создайте словарь, где ключами будут числа от 1 до 5, а значениями - их кубы, с помощью выражения-генератора.
# dict_out = {num: num ** 3 for num in range(1, 6)}
# print(dict_out)

# Создайте кортеж из строк, содержащих только гласные буквы, с помощью выражения-генератора.
# text = 'приветулька'
# set_out = tuple(let for let in text if let in 'ауеоуи')
# print(set_out)

# Создайте множество из всех гласных букв в строке "привет" с помощью set comprehension.
# text = 'приветулька'
# set_out = {let for let in text if let in 'ауеоуи'}
# print(set_out)

# Создайте множество из всех чисел от 1 до 50, которые делятся на 3 и 5, с помощью set comprehension.
# set_out = {num for num in range(1, 51) if num % 3 == 0 and num % 5 == 0}
# print(set_out)

# Создайте словарь, где ключами будут числа от 1 до 100, а значениями - их кубы, с помощью dictionary comprehension.
# dict_out = {num: num ** 3 for num in range(1, 101)}
# print(dict_out)

# from math import factorial
# # Создайте словарь, где ключами будут числа от 1 до 10, а значениями - их факториалы, с помощью dictionary comprehension.
# dict_out = {num: num * factorial(num - 1) if num > 0 else 1 for num in range(1, 11)}
# print(dict_out)

# итератор с помощью iter().
# Используйте next() для получения следующего элемента множества с помощью итератора.
# some_numbers = iter(range(1, 15))
# print(next(some_numbers))
# print(next(some_numbers))
# print(next(some_numbers))

#import itertools

# Создайте список из всех пар чисел от 1 до 5 с помощью выражения-генератора.
# list_out = list(itertools.product(range(1, 6), repeat=2))
# print(list_out)

# Создайте множество из всех возможных комбинаций чисел 1 и 2 длиной 3 с помощью выражения-генератора.
# list_out = list(itertools.product(range(1, 3), repeat=3))
# print(list_out)

import math
# Создайте множество из всех чисел от 1 до 100, которые являются степенями двойки, с помощью set comprehension.
# some_set = {num for num in range(1, 101) if num & (num - 1) == 0}
# print(some_set)

# Создайте множество из всех чисел от 1 до 50, которые являются квадратами целых чисел, с помощью set comprehension.
# some_set = {num ** 2 for num in range(1, 50)}
# print(some_set)

# Создайте список списков и получите его итератор с помощью iter().
#Используйте next() для получения следующего списка из списка списков с помощью итератора.
# some_spisok = iter([[2, 4, 6], [6, 8, 10], [15, 5, 10]])
# print(next(some_spisok))
# print(next(some_spisok))

# Создайте множество из всех нечетных чисел до 50 с помощью выражения-генератора.
# some_set = {num for num in range(1, 51) if num % 2 !=0}
# print(some_set)

# Создайте множество из всех чисел от 1 до 100, которые содержат цифру 3, с помощью set comprehension.
# n = str(3)
# some_set = {num for num in range(1, 101) if n in str(num)}
# print(some_set)

# Создайте множество из всех предложений в тексте с помощью set comprehension.
# text = 'We can learn it. I dont cry. We can learn it. I believe.'
# def set_for_text_sentence(some_text: str):
#    set_out = {words for words in text.split('. ')}
#    return set_out
# resalr = set_for_text_sentence(text)
# print(resalr)

# Создайте словарь, где ключами будут числа от 1 до 10, а значениями - список из их кубов и квадратов,
# с помощью dictionary comprehension.
# some_dict = {num: (num **2, num ** 3) for num in range(1,11)}
# print(some_dict)

# # Создайте словарь, где ключами будут числа от 1 до 50, а значениями - список из делителей чисел,
# с помощью dictionary comprehension.
# def find_divisors(number):
#     divisors = [num for num in range(1, number + 1) if number % num == 0]
#     return divisors
#
# dict_out = {num: find_divisors(num) for num in range(1, 51)}
# print(dict_out)
# тут конечно мда....)


# Создайте словарь, где ключами будут числа от 1 до 50, а значениями - True, если число простое, и False,
# если нет, с помощью dictionary comprehension.
# def is_prime(number):
#     if number < 2:
#         return False
#     for num in range(2, int(number**0.5) + 1):
#         if number % num == 0:
#             return False
#     return True
#
# dict_out = {num: is_prime(num)
#
# for num in range(1, 51)}
# print(dict_out) # не люблю простые числа((

# Создайте словарь, где ключами будут числа от 1 до 100, а значениями - их квадратные корни, с помощью dictionary comprehension.
# import math
# dict_out = {num: round(math.sqrt(num), 2) for num in range(1, 100)}
# print(dict_out)

# Создайте список из всех букв в верхнем регистре с помощью выражения-генератора.
# text = 'I like dogs. Cats dont like me. Rabbits dont like ANYONE!'
# list_out = [letter for letter in text if letter.istitle()]
# print(list_out)
