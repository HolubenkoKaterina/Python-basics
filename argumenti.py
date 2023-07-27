
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

# Упакуйте значения 10, 20 и 30 в кортеж и присвойте его переменной my_tuple.
# def pack_tuple(*args):
#     my_tuple = tuple(args)
#     return my_tuple
# resalt = pack_tuple(10, 20, 30 )
# print(resalt)

# Распакуйте строку "hello" и присвойте каждую букву переменным a, b, c, d, и e.
# def unpack_word(*args):
#     a, b, c, d, e = args
#     return args
# a, b, c, d, e = unpack_word(*'hello')
# print(a, b, c, d)

# Напишите функцию, которая принимает список строк и объединяет их в одну строку,
# используя определенный разделитель. Функция должна иметь возможность принимать различное количество аргументов.
# def union_strings_in_list(*args, serarator=' @ '):
#     return serarator.join(args)
# listik = ['lisa alisa', 'alisa lisa']
# resalt = union_strings_in_list(*listik)
# print(resalt)

# Реализуйте функцию, которая принимает несколько числовых аргументов и возвращает их среднее значение.
# def aver_from_list_numbers(*args):
#     return sum(args) / len(args)
# list_numbers = [2, 4, 6, 8, 10, -20]
# resalt = aver_from_list_numbers(*list_numbers)
# print(resalt)

# Создайте функцию, которая принимает произвольное количество аргументов и возвращает самый большой и самый маленький из них.
# def min_max_element(*args):
#     return max(args), min(args)
# spisok = [2, 15, -15]
# resalt = min_max_element(*spisok)
# print(resalt)

# Реализуйте генератор, который возвращает факториалы всех чисел от 1 до n (заданного аргументом).
# def factorial(n):
#     result = 1
#     for num in range(1, n + 1):
#         result *= num
#     return result
# n = 4
# print(factorial(n))

# Создайте генератор, который возвращает все слова из списка, имеющие длину больше заданного значения.
# def lenght_more(listik: list, lenght: int):
#     resalt = []
#     for elem in listik:
#         if len(elem) > lenght:
#             resalt.append(elem)
#     return resalt
#sp = ['lisa', 'world', 'python', 'one']
# resalt = lenght_more(sp, 5)
# print(resalt)

# def lenght_more(args, lenght: int):
#     resalt = [elem for elem in args if len(elem) > lenght]
#     return resalt
# resalt = lenght_more(sp, lenght=4)
# print(resalt)

# Упакуйте два значения 5 и 10 в список и присвойте его переменной my_list.
# def pack_numb(*args):
#     my_list = list(args)
#     return my_list
# sp = 4,5
# resalt = pack_numb(*sp)
# print(resalt)

# Распакуйте словарь {"name": "John", "age": 30, "city": "New York"} и присвойте
# ключ "name" переменной name, ключ "age" переменной age, и ключ "city" переменной city.
# dic = {"name": "John", "age": 30, "city": "New York"}
# def unpack_dict(args):
#     name = args['name']
#     age = args['age']
#     city = args['city']
#     return name, city, age
# resalt = unpack_dict(dic)
# print(resalt)

# Упакуйте значения 100, 200, и 300 в словарь, используя ключи "x", "y", и "z" соответственно,
# и присвойте его переменной my_dict.
# def pack_numb(x, y, z):
#     my_dict = {'x': x, 'y': y, 'z': z}
#     return my_dict
# resalt = pack_numb(100, 200, 300)
# print(resalt)

# Напишите функцию, которая принимает неограниченное количество строковых аргументов и возвращает список этих
# аргументов в верхнем регистре.
# sp = ['we like', 'he likes', 'she likes']
# def arg_upper(*args):
#     resalt = [elem.upper() for elem in args]
#     return resalt
# resalt = arg_upper(*sp)
# print(resalt)

# Реализуйте функцию, которая принимает произвольное количество числовых аргументов и возвращает их сумму и произведение.
# numbers = [4, 5, 7, 10]
# def summa_and_multiplace_numbers(*args):
#     mult = 1
#     summa = sum(args)
#     for num in args:
#        mult *= num
#     return (f' произведение {mult} , сумма {summa}')
# resalt = summa_and_multiplace_numbers(*numbers)
# print(resalt)

# Напишите функцию, которая принимает словарь и произвольное количество аргументов kwargs,
# и обновляет словарь значениями из kwargs.
# dict_in = {"name": "John", "age": 30}
# def update_dict(dict, **kwargs):
#     dict_out = dict.copy()
#     dict_out.update(kwargs)
#     return dict_out
# resalt = update_dict(dict_in, age=31, city='kyev')
# print(resalt)

# Реализуйте генератор, который возвращает все возможные комбинации из n элементов взятых по k.

#
# Создайте генератор, который принимает список списков и возвращает все элементы вложенных списков.
#
# Распакуйте список ["apple", "banana", "cherry"] в функции print(), чтобы вывести каждый элемент списка на отдельной строке.
# def unpack_list(*args):
#     for elem in args:
#         print(elem)
# spisok = ["apple", "banana", "cherry"]
# unpack_list(*spisok)
#
# Упакуйте первые 3 числа Фибоначчи в множество и присвойте его переменной fibonacci_set.
# def pack_nums_fibonacci_in_set(n):
#     fibonacci_set = set()
#     a, b = 0, 1
#     for _ in range(n):
#         fibonacci_set.add(a)
#         a, b = b, a + b
#     return fibonacci_set
#
# result = pack_nums_fibonacci_in_set(25)
# print(result)
# что это такое???? я не знала таких формул...

# Распакуйте кортеж (1, 2, 3, 4, 5) в функции sum() и вычислите сумму элементов кортежа.
# data = (1, 2, 3, 4, 5)
# def unpack_tuple_to_sum(*args):
#     summa = sum(args)
#     return (f'{summa} это сумма всех элементов в кортеже {data}')
# resalt = unpack_tuple_to_sum(*data)
# print(resalt)

# Создайте функцию, которая принимает несколько числовых аргументов и возвращает их сумму и количество.
# data = (1, 2, 3, 4, 5)
# def summa_and_count_element(*args):
#     summa = sum(args)
#     counts = len(args)
#     return (f'{summa} это сумма, а это кол-во элементов {counts}')
# resalt = summa_and_count_element(*data)
# print(resalt)

# Реализуйте функцию, которая принимает несколько строковых аргументов и возвращает объединенную строку с удаленными пробелами.
# sp = ['we like', 'he likes', 'she likes']
# def union_delete_probel(*args, sep=''):
#     result = sep.join(arg.replace(' ', '') for arg in args)
#     return result
# resalt = union_delete_probel(*sp)
# print(resalt)
#
# Напишите функцию, которая принимает неограниченное количество списков и объединяет их в один список.
# list_of_lists = [[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6]]
# def union_lists_into_one(*args):
#     list_out = []
#     for elements in args:
#         for element in elements:
#             list_out.append(element)
#     return list_out
# resalt = union_lists_into_one(*list_of_lists)
# print(resalt)

# Создайте генератор, который возвращает все уникальные элементы из списка списков.
# list_of_lists = [[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6]]
# def unique_elements_from_list(*args):
#     unique = set()
#     for inner_list in args:
#         for elem in inner_list:
#             unique.add(elem)
#     return list(unique)
# resalt = unique_elements_from_list(*list_of_lists)
# print(resalt)
# Реализуйте генератор, который возвращает все значения по ключу "key" из списка словарей.

# Напишите генератор, который возвращает все числа от 1 до n, исключая числа, которые делятся на заданное число k.
# resalt = lambda n, k: (num for num in range(1, n+1) if num % k != 0)
# resalt = list(resalt(10, 6))
# print(resalt)

# Упакуйте значения 3, 6 и 9 во множество и присвойте его переменной my_set.
# def pack_numbers_in_set(*args):
#     my_set = []
#     for element in args:
#         my_set.append(element)
#     return set(my_set)
# print(pack_numbers_in_set(3, 6, 9))

# Распакуйте строку "hello" в функции list() и преобразуйте ее в список символов.
# def unpack_strings_in_list(*args):
#     list_out = []
#     for elements in args:
#         for letters in elements:
#             list_out.append(letters)
#     return list_out
# resalt = unpack_strings_in_list('hello world')
# print(resalt)

# Упакуйте значения "red", "green" и "blue" в кортеж и присвойте его переменной colors.
# def pack_values(*args):
#     colors = tuple(args)
#     return colors
# resalt = pack_values("red", "green" ,"blue")
# print(resalt)