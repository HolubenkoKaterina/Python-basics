# Реализуйте функцию, которая генерирует квадраты всех чисел в диапазоне от 1 до N.
# def generator(finish):
#     for elem in range(1, finish + 1):
#         yield elem ** 2
# result = generator(10)
# # Print squares
# # for square in result:
# #     print(square)
# print(next(result))  # Печатает квадрат числа 1
# print(next(result))  # Печатает квадрат числа 2

# Напишите генератор, который выдает случайные числа от 1 до 100.
# import random
# def generator():
#     while True:
#         yield random.randint(1, 100)
# resalt = generator()
# print(next(resalt))
# print(next(resalt))

# Создайте генератор, который производит все строки из заданного списка строк.
# list_1 = ["apple", "banana", "date", "kiwi"]
# def generator_strings(list_1):
#     for elem in list_1:
#         yield elem
# resalt = generator_strings(list_1)
# print(next(resalt))
# print(next(resalt))

# Напишите функцию, которая генерирует бесконечную последовательность букв алфавита.
# import string
# def generator():
#     for letter in string.ascii_letters:
#         yield letter
# resalt = generator()
# print(next(resalt))
# print(next(resalt))

# Реализуйте генератор, который производит все целые числа в заданном диапазоне.
# import random
# def generator(start, finish):
#     for elem in range(start, finish + 1):
#         yield elem
# resalt = generator(1, 15)
# print(next(resalt))
# print(next(resalt))


# Напишите функцию, которая генерирует все числа, у которых сумма цифр делится на заданное число.
#
# Реализуйте генератор, который генерирует случайные имена для людей.
#
# Реализуйте генератор, который генерирует случайные числа в заданном диапазоне с заданным шагом.
#
# Реализуйте генератор, который выдает случайные буквы и цифры.
# import string
# import itertools
# def generator():
#     for elem in itertools.chain(string.digits, string.ascii_letters):# itertools.chain обьединение нескольких последовательностей в одну
#         yield elem
# resalt = generator()
# print(next(resalt))
# print(next(resalt))

# Создайте генератор, который производит все простые числа в двоичной системе счисления.
# def generate_primes(start, finish):
#     def is_prime(num):
#         if num < 2:
#             return False
#         for i in range(2, int(num ** 0.5) + 1):
#             if num % i == 0:
#                 return False
#         return True
#
#     for num in range(start, finish+1):
#         if is_prime(num):
#             yield num
#
# primes_generator = generate_primes(10, 30)
# for prime in primes_generator:
#     print(prime)

# Напишите генератор, который генерирует случайные координаты на плоскости (x, y) в заданном диапазоне.
# import random
# def generate_coordinates(min_x, max_x, min_y, max_y):
#     while True:# генерация случайного числа с большим числом после ","
#         yield (random.uniform(min_x, max_x), random.uniform(min_y, max_y))
#
# coordinates_generator = generate_coordinates(0, 10, 0, 10)
# for _ in range(10):
#     x, y = next(coordinates_generator)
#     print(f"({x}, {y})")

# Создайте генератор, который генерирует случайные IP-адреса.
# import random
# def generate_ip():
#     return f"{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"
# ip_generator = (generate_ip() for _ in range(10))  # Генерируем 10 случайных IP-адресов
# for ip in ip_generator:
#     print(ip)