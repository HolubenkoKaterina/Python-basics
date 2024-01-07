# 21. Примени функцию map для объединения каждой строки в списке с её обратной версией.
# string = 'hello and doing homework'
# str_out = string + ' ' + ' '.join(map(lambda x: x[::-1], string.split()))
# print(str_out)

# 22. Используй map для вычисления факториала каждого числа в списке.
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
#
# nums = [5, 2, 3]
# factorials = list(map(factorial, nums))
# print(factorials)

# 23. Примени map для конвертации каждой строки числа в списке в римское число.
# import roman
import random
# nums = random.sample(range(1, 18), random.randint(5, 11))
# print(nums)
# def convert_roman_nums(list_nums: list):
#
#     list_out = list(map(lambda num: roman.toRoman(num), list_nums))
#     return list_out
# print(convert_roman_nums(nums))

# 24. Используй map для преобразования каждого элемента списка в его строковое представление и добавления префикса "Element_".
# nums = random.sample(range(1, 18), random.randint(5, 11))
# resalt = list(map(lambda num: ('Element_' + str(num)), nums))
# print(resalt)

# 25. Примени функцию map для вычисления суммы цифр в каждом числе списка.
# nums = random.sample(range(1, 18), random.randint(5, 11))
# print(nums)
# def sums_digits_number(nums: list):
#     list_out = []
#     for num in nums:
#         if num <= 9:
#             list_out.append(num)
#         else:
#             # Преобразование числа в строку и вычисление суммы цифр
#             digit_sum = sum(int(digit) for digit in str(num))
#             list_out.append(digit_sum)
#     return list_out
#
# result = sums_digits_number(nums)
# print(result)

# # 26. Используй map для замены каждой строки в списке на её хэш-значение.
# text_list = ['i', 'like', 'python!']
# text_out = list(map(lambda elem: hash(elem), text_list))
# print(text_out)

# 27. Примени map для удаления пробелов из каждой строки в списке.
# example_strings = ["  hello  ", " world ", "example "]
# list_out = list(map(lambda elem: elem.strip(), example_strings))
# print(list_out)

# 28. Используй map для преобразования каждого числа в списке в его шестнадцатеричное представление.
# nums = random.sample(range(1, 18), random.randint(5, 11))
# print(nums)
# nums_new = list(map(lambda num: hex(num), nums))
# print(nums_new)

# 29. Примени функцию map для умножения каждого чётного числа в списке на 3, а каждого нечётного на 2.
# import random
#
# nums = random.sample(range(1, 18), random.randint(5, 11))
# print(nums)
#
# def multiply_nums(num):
#     if num % 2 == 0:
#         return num * 3
#     else:
#         return num * 2
#
# list_out = list(map(multiply_nums, nums))
# print(list_out)

# 30. Используй map для объединения каждого элемента списка с его индексом в формате "Index: Element".
# nums = random.sample(range(1, 18), random.randint(5, 11))
# print(nums)
# def index_num(enumerated_item):
#     ind, num = enumerated_item
#     return f'{ind}: {num}'
#
# result = list(map(index_num, enumerate(nums)))
# print(result)


