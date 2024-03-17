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