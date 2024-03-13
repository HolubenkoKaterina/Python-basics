
# Напишите функцию, которая принимает неограниченное количество аргументов *args и возвращает их сумму.
# spisok = [2, 4, 6, 8, 10, 12, 15, 25]
# def sum_numbers(*args):
#     return sum(args)
# resalt = sum_numbers(*spisok)
# print(resalt)

# Напишите функцию, которая принимает неограниченное количество аргументов *args и возвращает их произведение.
# def multiplace_numbers(*args):
#     resalt = 1
#     for number in args:
#         resalt *= number
#     return resalt
# spisok = [2, 4, 6, 8, 10, 12, 15, 25]
# resalt = multiplace_numbers(*spisok)
# print(resalt)

# Создайте функцию, которая принимает произвольное количество аргументов *args и выводит их типы.
# def type_arguments(*args):
#     for element in args:
#         print(type(element))
# spisok = [2, 4, 'book']
# resalt = type_arguments(*spisok)
# print(resalt)

# Реализуйте генератор, который возвращает все четные числа от 1 до 100.
# resalt = [number for number in range(0, 2, 101) if number % 2 == 0]
# print(resalt)

# Напишите генератор, который возвращает все нечетные числа от 1 до 100.
# resalt = [number for number in range(1, 101, 2) if number % 2 != 0]
# print(resalt)

# Создайте генератор, который возвращает все числа в интервале [start, end], заданном аргументами функции.
# def numbers_from_to_end(start, end):
#     return [number for number in range(start, end)]
# resalt = numbers_from_to_end(2, 5)
# print(resalt)

# Распакуйте список [1, 2, 3] и присвойте переменным a, b, и c соответствующие значения.
# def unpack_list(a, b, c):
#     print(f'a: {a}, b: {b}, c: {c}')
# listik = [1, 2, 3]
# unpack_list(*listik)


