# Создайте декоратор, который проверяет, что переданный аргумент больше заданного значения.
'''def decorator(value):
    def decorator_inner(func):
        def wrapper(*args, **kwargs):
            for arg in args:
                if isinstance(arg, (list, tuple, str)):
                    for elem in arg:
                        if isinstance(elem, int):
                            if value <= elem:
                                raise ValueError('значение превышает указанное')
                            else:
                                return func(*args, **kwargs)
                        else:
                            raise ValueError('не тот тип данных')
        return wrapper
    return decorator_inner
@decorator(value=4)

def summa(*args):
    summa = 0
    for arg in args:
        for ele in arg:
            if isinstance(ele, int):
                summa += ele
    return summa
lisat_num = [5, 4]
resalt = summa(lisat_num)
print(resalt)'''
# # Создайте декоратор, который принимает список чисел и умножает результат функции на все элементы этого списка.
'''# def decorator():
#
#     def actual_decorator(func):
#         def wrapper(*args, **kwargs):
#             result = func(*args, **kwargs)
#             for el in spisok:
#                 if type(el) == int:
#                     result *= el
#                 elif isinstance(el, str) and el.isdigit():
#                     result *= int(el)
#                 else:
#                     raise ValueError('тип данных не числовой!')
#             return result
#         return wrapper
#     return actual_decorator
#
# @decorator(spisok=data)
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
