# Убедитесь, что все элементы списка удовлетворяют определенному условию (например, больше 42).
# import random
# my_list = random.sample(range(-5, 55), random.randint(5, 10))
# print(my_list)
# resalt = all(elem > 42 for elem in my_list)
# print(resalt)
import random

# Проверьте, все ли элементы списка начинаются с определенной буквы.
# my_strings = ["apple", "banana", "cherry", "date"]
# letter = 'a'
# resalt = all(elem.startswith('letter') for elem in my_strings)
# print(resalt)

# Убедитесь, что все элементы списка не содержат определенного символа.
# my_strings = ["apple", "banana", "date"]
# letter = 'a'
# resalt = all(letter in elem for elem in my_strings)
# print(resalt)

# Проверьте, все ли элементы списка являются простыми числами.
# import random
# my_list = random.sample(range(-5, 55), random.randint(5, 10))
# def is_prime(num):
#    if num < 2:
#        return False
#    for i in range(2, int(num**0.5) + 1):
#        if num % i == 0:
#            return False
#    return True
# all_prime = all(is_prime(num) for num in my_list)
# if all_prime:
#     print("Все числа в списке являются простыми.")
# else:
#     print("Не все числа в списке являются простыми.")


# Убедитесь, что все элементы списка являются строками.
# my_strings = ["apple", "banana", "date", 4]
# resalt = all(type(elem) == str for elem in my_strings)
# print(resalt)

# Проверьте, все ли элементы списка являются дробными числами.
# my_list = random.sample(range(-5, 55), random.randint(5, 10))
# resalt = all(type(elem) == float for elem in my_list)
# print(resalt)

# Убедитесь, что все элементы списка являются положительными.
# resalt = all(elem > 0 for elem in my_list)
# print(resalt)
# Проверьте, все ли элементы списка являются отрицательными.
# resalt = all(elem < 0 for elem in my_list)
# print(resalt)

# Убедитесь, что все элементы списка содержат только буквы (без цифр и символов).
# my_strings = ["apple", "banana", "date", 4]
# resalt = all(elem.isdigit() for elem in my_strings)
# print(resalt)

# Проверьте, все ли элементы списка содержат хотя бы одну цифру.
# my_strings = ["apple", "banana", "date", 4]
# resalt = all(elem.isnumeric() for elem in my_strings)
# print(resalt)

# Убедитесь, что все элементы списка не пусты.
# my_strings = ["apple", "banana", "date"]
# resalt = all(len(elem) > 0 for elem in my_strings)
# print(resalt)

# Проверьте, все ли элементы списка оканчиваются на определенную букву.
# my_strings = ["apple", "banana", "date", 4]
# letter = 'e'
# resalt = all(elem.endswith(letter) for elem in my_strings)
# print(resalt)

# Убедитесь, что в списке есть хотя бы один элемент, содержащий только цифры.
# my_strings = ["apple", "banana", "date", 4]
# resalt = any(elem.isnumeric() for elem in my_strings if isinstance(elem, str))
# print(resalt)

# Проверьте, есть ли в списке хотя бы один элемент, являющийся палиндромом (читается одинаково с начала и с конца).
# my_strings = ["apple", "banana", "date", 4]
# resalt = any(elem == elem[::-1] for elem in my_strings if isinstance(elem, str))
# print(resalt)

# Убедитесь, что в списке есть хотя бы один элемент, начинающийся с определенного префикса.
# my_strings = ["apple", "banana", "date", 4]
# start = 'ap'
# resalt = any(elem.startswith(start) for elem in my_strings if isinstance(elem, str))
# print(resalt)

# Проверьте, есть ли в списке хотя бы один элемент, оканчивающийся определенным суффиксом.
# my_strings = ["apple", "banana", "date", 4]
# finish = 'le'
# resalt = any(elem.endswith(finish) for elem in my_strings if isinstance(elem, str))
# print(resalt)

# Убедитесь, что в списке есть хотя бы один элемент, содержащий только буквы и цифры.
# my_strings = ["ap4ple", "banana", "date", 4]
# resalt = any(elem.isalpha() for elem in my_strings if isinstance(elem, str))
# print(resalt)

# Проверьте, есть ли в списке хотя бы один элемент, являющийся степенью двойки.
# import math
# my_list = random.sample(range(-5, 55), random.randint(5, 10))
# print(my_list)
# resalt = any(math.log(elem, 2) for elem in my_list if isinstance(elem, int))
# print(resalt)

# Убедитесь, что в списке есть хотя бы один элемент, состоящий только из символов пунктуации.
# import string
# my_strings = ["ap4ple", "banana", "date", 4]
# resalt = any(all(char in string.punctuation for char in elem) for elem in my_strings if isinstance(elem, str))
# print(resalt)

# Убедитесь, что в списке есть хотя бы один элемент, который меньше среднего значения списка.
# summa = 0
# lenght = len(my_list)
# for elem in my_list:
#     summa += elem
#     aver = round((summa / lenght), 2)
#     resalt = any(elem > aver for elem in my_list)
# print(f'результат {resalt}, среднее значение {aver}')
