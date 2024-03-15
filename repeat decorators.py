# Создайте декоратор, который повторяет выполнение функции заданное количество раз и выводит среднее время выполнения.
'''# import time
#
# def decorator(n):
#     def decorator_inner(func):
#         def wrapper(*args, **kwargs):
#             total_execution_time = 0
#
#             for _ in range(n):
#                 start = time.time()
#                 result = func(*args, **kwargs)
#                 finish = time.time()
#                 execution_time = finish - start
#                 total_execution_time += execution_time
#
#                 #print(f"Время выполнения {func.__name__}: {execution_time:.6f} секунд")
#
#             average_execution_time = total_execution_time / n
#             print(f"Среднее время выполнения {func.__name__}: {average_execution_time:.6f} секунд")
#
#             return result
#
#         return wrapper
#     return decorator_inner
#
# @decorator(n=5)
# def summa(a, b):
#     return a + b
#
# result = summa(4, 10)
# print(result)'''
# Создайте декоратор, который заменяет все гласные буквы в результате выполнения функции на '*'.
'''#def decorator(letter):
#     def decorator_inner(func):
#         def wrapper(*args, **kwargs):
#             result = func(*args, **kwargs)
# 
#             if isinstance(result, str):
#                 result = result.lower()
#                 result = result.replace(letter, '*')
#             else:
#                 raise ValueError('не тот тип данных')
#             return result
# 
#         return wrapper
# 
#     return decorator_inner
# 
# 
# @decorator(letter='l')
# def text(some_text: str):
#     return some_text
# 
# 
# data = ['i like python']
# result = text(data)
# print(result)'''