# Вычислите факториал числа.
# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial((n-1))
# print(factorial(5))

# Расчет чисел Фибоначчи.
# def fibonacci(n):
#     if n == 0:
#         return [0]
#     elif n == 1:
#         return [0, 1]
#     else:
#         fib_list = fibonacci(n - 1)
#         fib_list.append(fib_list[-1] + fib_list[-2])
#         return fib_list
#
# result = fibonacci(5)
# print(result)


# Подсчет суммы цифр в числе.
# def summa_numbers_in_num(n):
#     if 1 <= n <= 9:
#         return n
#     else:
#         last_digit = n % 10  # Get the last digit
#         rest_of_number = n // 10  # Get the rest of the number without the last digit
#         return last_digit + summa_numbers_in_num(rest_of_number)  # Recursively call the function with the rest of the number
# result = summa_numbers_in_num(54687867)
# print(result)  # Outputs: 15 (1 + 2 + 3 + 4 + 5)

# Вывод чисел от 1 до N в порядке возрастания.
# def print_num_up(n):
#     if n == 1:
#         return [n]
#     else:
#         return print_num_up(n - 1) + [n]
#
# result = print_num_up(10)
# print(result)

# Вывод чисел от N до 1 в порядке убывания.
# def print_num_down(n):
#     if n == 1:
#         return [n]
#     else:
#         return [n] + print_num_down(n - 1)
# print(print_num_down(10))

# Проверка, является ли строка палиндромом.
# text = 'mamam'
# def check(text):
#     if len(text) == 0:
#         return True
#     else:
#         return text[0] == text[-1] and check(text[1:-1])
# print(check(text))

# Рекурсивная проверка сортировки массива.
# elements = [2, 4, 6, 8]
# def check_sorted(some_list: list):
#     if len(some_list) <= 1:
#         return True
#     for i in range(len(some_list) - 1):
#         if some_list[i] > some_list[i + 1]:
#             return False
#
#     return True
# print(check_sorted(elements))