# Напишите декоратор, который принимает параметр "message" и выводит это сообщение перед выполнением функции.
'''# def decorator_out (message):
#     def decorator(func):
#         def wrapper( *args, **kwargs):
#             print(message)
#             resalt = func(*args, **kwargs)
#             return resalt
#         return wrapper
#     return decorator
# @decorator_out(message='а вот и наше сообщение!')
#
# def summa(*args):
#     total_sum = 0
#     for arg in args:
#         if isinstance(arg, (list, tuple)):
#             for el in arg:
#                 if isinstance(el, int):
#                     total_sum += el
#                 if isinstance(el, str):
#                     if el.isdigit():
#                         total_sum += int(el)
#     return total_sum
#
#
# data2 = ('10', '10', 15)
# result = summa(data2)
# print(result)'''
# Создайте декоратор, который принимает параметр "log_file" и записывает лог выполнения функции в указанный файл.
'''def decorator(file_name):
    def decorator_inner(func):
        def wrapper(*args, **kwargs):
            resalt = func(*args, **kwargs)
            with open(file_name, 'w', encoding='utf-8') as my_file:
               my_file.write(f"Вызвана функция {func.__name__} с аргументами {args} и результатом {resalt}\n")
            return resalt
        return wrapper
    return decorator_inner
@decorator(file_name='file_file.log')
def summa(*args):
    summa = 0
    for arg in args:
        for ele in arg:
            if isinstance(ele, int):
                summa += ele
    return f'{summa} сумма которая получилась'
lisat_num = [5, 4]
resalt = summa(lisat_num)
print(resalt)'''
