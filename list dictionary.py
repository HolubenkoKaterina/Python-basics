# 1. Создайте список словарей, представляющих информацию о разных людях (имя, возраст, место жительства).
# 2. Найдите средний возраст людей из списка.
# people_list = [
#     {'name': 'Анна', 'age': 25, 'location': 'Москва'},
#     {'name': 'Иван', 'age': 30, 'location': 'Санкт-Петербург'},
#     {'name': 'Елена', 'age': 35, 'location': 'Новосибирск'}
# ]
# def get_aver_age(my_data: list):
#     summa = 0
#     for elem in my_data:
#         name = elem['name']
#         age = int(elem['age'])
#         location = elem['location']
#         summa += age
#     aver = round(summa / len(my_data), 2)
#     return aver
# print(get_aver_age(people_list))

# def get_people_upper_aver_age(my_data: list):
#     list_people_upper_aver_age = {}
#     resalt = get_aver_age(my_data)
#     for elem in my_data:
#         name = elem['name']
#         age = int(elem['age'])
#         if age >= resalt:
#             list_people_upper_aver_age[name] = age
#     return list_people_upper_aver_age
# print(get_people_upper_aver_age(people_list))

# 3. Выведите имена людей, младше 30 лет.
# def get_people(my_data: list):
#     list_people = {}
#     for elem in my_data:
#         name = elem['name']
#         age = int(elem['age'])
#         if age < 30:
#             list_people[name] = age
#     return list_people
# print(get_people(people_list))

# 4. Отсортируйте список по возрасту (от младшего к старшему).
# def sorted_list(my_data: list):
#     dict_out = {}
#     for elem in my_data:
#         name = elem['name']
#         age = int(elem['age'])
#         dict_out[name] = age
#         resalt = sorted(dict_out.items(), key=lambda elem: elem[1])
#     return resalt
# print(sorted_list(people_list))

# 5. Подсчитайте количество людей из одного и того же города.
# def count_people(my_data: list, city):
#     counter = 0
#     for elem in my_data:
#         location = elem['location'].lower()
#         if location == city.lower():
#             counter += 1
#     return counter
# print(count_people(people_list, city='Новосибирск'))

# 6. Найдите самого старшего человека в списке.
# 7. Найдите самого молодого человека в списке.
# def find_oldest_yang_person(my_data: list):
#     old_person = ''
#     yang_person = ''
#     max_age = float('-inf')
#     min_age = float('inf')
#     for elem in my_data:
#         name = elem['name']
#         age = int(elem['age'])
#         if age < min_age:
#             min_age = age
#             yang_person = name
#         if age > max_age:
#             old_person = name
#             max_age = age
#     return f'{min_age} самый младший , {yang_person} его имя\n{max_age} самый старший, {old_person} его имя'
# print(find_oldest_yang_person(people_list))

# 8. Создайте новый список, содержащий только людей из определенного города.
people_list = [
    {'name': 'John Doe', 'age': 35, 'location': 'New York, USA', 'gender': 'Male'},
    {'name': 'Jane Smith', 'age': 28, 'location': 'New York, USA', 'gender': 'Female'},
    {'name': 'Michael Johnson', 'age': 35, 'location': 'Cairo, Egypt', 'gender': 'Male'},
    {'name': 'Sophia Kim', 'age': 32, 'location': 'Seoul, South Korea', 'gender': 'Female'},
    {'name': 'Mohammed Ali', 'age': 29, 'location': 'Dubai, UAE', 'gender': 'Male'},
    {'name': 'Maria Rodriguez', 'age': 31, 'location': 'Madrid, Spain', 'gender': 'Female'},
    {'name': 'Yuki Tanaka', 'age': 27, 'location': 'Tokyo, Japan', 'gender': 'Female'},
    {'name': 'Ahmed Hassan', 'age': 34, 'location': 'Cairo, Egypt', 'gender': 'Male'}
]

# def get_data_from_city(my_list: list):
#     dict_people_counter = {}
#     for elem in my_list:
#         counter = 0
#         adress = elem['location']
#         counter += 1
#         if adress not in dict_people_counter:
#             dict_people_counter[adress] = 1
#         else:
#             dict_people_counter[adress] += 1
#     return dict_people_counter
# print(get_data_from_city(people_list))

# 9. Подсчитайте количество людей разного возраста.
# def count_some_age(my_list: list):
#     dict_people_counter = {}
#     for elem in my_list:
#         counter = 0
#         age = elem['age']
#         counter += 1
#         if age not in dict_people_counter:
#             dict_people_counter[age] = 1
#         else:
#             dict_people_counter[age] += 1
#     return dict_people_counter
# print(count_some_age(people_list))

# 10. Найдите средний возраст людей из определенного города.
# def aver_age_people(my_list: list):
#     summa = 0
#     aver = 0
#     for elem in my_list:
#         age = int(elem['age'])
#         summa += age
#         aver = round(summa / len(my_list), 2)
#     return aver
# print(aver_age_people(people_list))

# def find_aver_age_in_city(my_list: list):
#     dict_age_city = {}
#     summa = 0
#     aver = 0
#     count = 0
#     for elem in my_list:
#         adress = elem['location']
#         age = elem['age']
#         summa += age
#         count += 1
#         if adress not in dict_age_city:
#             dict_age_city[adress] = {'summa': summa, 'count': count}
#         else:
#             dict_age_city[adress]['summa'] += summa
#             dict_age_city[adress]['count'] += count
#     for city, data in dict_age_city.items():
#         data['average'] = round(data['summa'] / data['count'], 2)
#         data.pop('summa')
#         data.pop('count')
#
#     return dict_age_city
#
# print(find_aver_age_in_city(people_list))

# 11. Добавьте нового человека в список.
# def add_person(my_list: list, name, age, location):
#     new_person = {'name': name, 'age': age, 'location': location }
#     my_list.append(new_person)
#     return my_list
# print(add_person(people_list, name='kat', age=30, location='kiev'))

# 12. Удалите человека из списка по имени.
# def del_person(my_list: list, name_del):
#     list_out = []
#     for elem in my_list:
#         name = elem['name'].lower()
#         if name_del != name:
#             list_out.append(elem)
#     return list_out
# print(del_person(people_list, name_del='kat'))

# 13. Измените место жительства определенного человека.
# def change_adress(my_list: list, name_find, adress_change):
#     for elem in my_list:
#         name = elem['name'].lower()
#         adress = elem['location']
#         if name == name_find.lower():
#             elem['location'] = adress_change
#     return my_list
# print(change_adress(people_list, name_find='John Doe', adress_change='new adress'))

# 14. Проверьте, есть ли в списке люди из определенного города.
# def check_person_from_some_city(my_list: list, city_check):
#     list_from_city = []
#     for elem in my_list:
#         name = elem['name']
#         adress = elem['location']
#         if city_check.lower() in adress.lower():
#             list_from_city.append((name, adress))
#     return list_from_city
#
# print(check_person_from_some_city(people_list, city_check='new York'))

# 15. Проверьте, есть ли в списке люди с определенным именем.
# def check_name_in_list(my_list: list, name_check):
#     list_name = []
#     for elem in my_list:
#         name = elem['name'].lower()
#         if name_check.lower() in name:
#             list_name.append(name)
#     return list_name
#
# print(check_name_in_list(people_list, name_check='Jane'))

# 16. Создайте копию списка и отсортируйте ее по имени.
# def sort_list(my_list: list):
#     list_new = sorted(my_list, key=lambda elem: elem['name'])
#     return list_new
# print(sort_list(people_list))

# 17. Найдите человека с самым длинным именем.
# def find_longest_name(my_list: list):
#     max_lenght = float('-inf')
#     name_longest = ''
#     for elem in my_list:
#         name = elem['name']
#         if len(name) > max_lenght:
#             max_lenght = len(name)
#             name_longest = name
#     return f'{name_longest} {max_lenght}'
# print(find_longest_name(people_list))

# 18. Создайте новый список, содержащий только имена людей.
# def names_from_list(my_list: list):
#     list_name = []
#     for elem in my_list:
#         name_full = elem['name']
#         name = name_full.split()
#         list_name.append(name[0])
#     return list_name
# print(names_from_list(people_list))

# 19. Создайте словарь, в котором ключами являются имена, а значениями — возраст.
# def get_dict_name_age(my_list: list):
#     dict_name_age = {}
#     for elem in my_list:
#         name_full = elem['name']
#         age = elem['age']
#         dict_name_age[name_full] = age
#     return dict_name_age
# print(get_dict_name_age(people_list))

# 20. Удалите людей старше 40 лет из списка.
# def del_some_people_upper_age(my_list: list, age_del):
#     list_out = [elem for elem in my_list if elem['age'] <= age_del]
#     return list_out
# print(del_some_people_upper_age(people_list, age_del=30))

# 21. Найдите средний возраст мужчин и женщин в списке.
# def aver_age_gender(my_list: list):
#     dict_age = {}
#     summa_men = 0
#     summa_women = 0
#     aver_age = 0
#     counter_men = 0
#     counter_women = 0
#     for elem in my_list:
#         age = int(elem['age'])
#         gender = elem['gender']
#         if gender == 'Male':
#             summa_men += age
#             counter_men += 1
#         else:
#             summa_women += age
#             counter_women += 1
#         if counter_men > 0:
#             dict_age['Male'] = summa_men / counter_men
#
#         if counter_women > 0:
#             dict_age['Female'] = summa_women / counter_women
#
#     return dict_age
#
# print(aver_age_gender(people_list))

# 22. Отсортируйте список по месту жительства.
# def sorted_list_people(my_list: list):
#     new_list = sorted(my_list, key=lambda elem: elem['location'])
#     return new_list
# print(sorted_list_people(people_list))

# 23. Создайте новый список, содержащий только людей, у которых имена начинаются на определенную букву.
# def name_list(my_list: list, letter_begin):
#     list_out = []
#     for elem in my_list:
#         full_name = elem['name'].split()
#         name = full_name[0].lower()
#         if name.startswith(letter_begin.lower()):
#             list_out.append(' '.join(full_name))
#     return list_out
# print(name_list(people_list, letter_begin='m'))

# 24. Подсчитайте, сколько раз каждое имя встречается в списке.
# def counter_name(my_list: list):
#     dict_out = {}
#     for elem in my_list:
#         counter = 0
#         full_name = elem['name'].split()
#         name = full_name[0].lower()
#         if name not in dict_out:
#             dict_out[name] = 1
#         else:
#             dict_out[name] += 1
#     return dict_out
# print(counter_name(people_list))

# 25. Найдите двух людей с самым близкими по возрасту днями рождения.
# people_list_new = [
#     {'name': 'John Doe', 'age': 35, 'location': 'New York, USA', 'gender': 'Male', 'date_of_birth': '1988-05-15'},
#     {'name': 'Jane Smith', 'age': 28, 'location': 'New York, USA', 'gender': 'Female', 'date_of_birth': '1993-02-22'},
#     {'name': 'Michael Johnson', 'age': 35, 'location': 'Cairo, Egypt', 'gender': 'Male', 'date_of_birth': '1988-09-10'},
#     {'name': 'Sophia Kim', 'age': 32, 'location': 'Seoul, South Korea', 'gender': 'Female', 'date_of_birth': '1991-11-30'},
#     {'name': 'Mohammed Ali', 'age': 29, 'location': 'Dubai, UAE', 'gender': 'Male', 'date_of_birth': '1994-07-03'},
#     {'name': 'Maria Rodriguez', 'age': 31, 'location': 'Madrid, Spain', 'gender': 'Female', 'date_of_birth': '1990-03-17'},
#     {'name': 'Yuki Tanaka', 'age': 27, 'location': 'Tokyo, Japan', 'gender': 'Female', 'date_of_birth': '1995-01-25'},
#     {'name': 'Ahmed Hassan', 'age': 34, 'location': 'Cairo, Egypt', 'gender': 'Male', 'date_of_birth': '1989-08-05'},
#     {'name': 'Carlos Martinez', 'age': 30, 'location': 'Madrid, Spain', 'gender': 'Male', 'date_of_birth': '1993-04-12'},
#     {'name': 'Yulia Ivanova', 'age': 33, 'location': 'Moscow, Russia', 'gender': 'Female', 'date_of_birth': '1988-06-20'},
#     {'name': 'Ivan Petrov', 'age': 37, 'location': 'Moscow, Russia', 'gender': 'Male', 'date_of_birth': '1984-09-28'},
#
# ]
# import datetime
#
# def find_birthday_min_difference(my_list: list):
#     min_difference = float('inf')
#     pair = []
#     for i in range(len(my_list)):
#         for j in range(i+1, len(my_list)):
#             if 'date_of_birth' in my_list[i] and 'date_of_birth' in my_list[j]:
#                 birthday_1 = datetime.datetime.strptime(my_list[i]['date_of_birth'], '%Y-%m-%d')
#                 birthday_2 = datetime.datetime.strptime(my_list[j]['date_of_birth'], '%Y-%m-%d')
#                 difference = abs((birthday_1 - birthday_2).days)
#                 if difference < min_difference:
#                     min_difference = difference
#                     pair = [my_list[i]['name'], my_list[j]['name']]
#
#     return pair, min_difference
#
# print(find_birthday_min_difference(people_list_new))

# 26. Создайте новый список, содержащий только людей, родившихся в определенный месяц.
# import datetime
# def list_people_in_some_month(some_list: list, month_filter:int):
#     list_out = []
#     for elem in some_list:
#         name = elem['name']
#         birthday = elem['date_of_birth']
#         new_birht = datetime.datetime.strptime(birthday, '%Y-%m-%d')
#         if month_filter == new_birht.month:
#             list_out.append(name)
#     return list_out
# print(list_people_in_some_month(people_list_new, month_filter=6))

# 27. Найдите людей, чьи имена содержат определенное слово.
# def get_list_people(my_list: list, name_find):
#     list_out = []
#     for elem in my_list:
#         name = elem['name'].lower()
#         if name_find.lower() in name:
#             list_out.append(name)
#     return list_out
# print(get_list_people(people_list_new, name_find='yu'))

# 28. Создайте новый список, содержащий только уникальные места жительства.
# def get_unique_location(my_list: list, locations):
#     list_out = []
#     for elem in my_list:
#         adress = elem['location'].lower()
#         if locations.lower() in adress:
#             if locations.lower() not in list_out:
#                 list_out.append(adress)
#             else:
#                 pass
#
#     return list_out
# print(get_unique_location(people_list_new, 'co'))

# 29. Найдите человека с наибольшей разницей в возрасте среди остальных.
import datetime
people_list_new = [
    {'name': 'John Doe', 'age': 35, 'location': 'Manhattan, New York, USA', 'gender': 'Male', 'date_of_birth': '1988-05-15'},
    {'name': 'Jane Smith', 'age': 28, 'location': 'Brooklyn, New York, USA', 'gender': 'Female', 'date_of_birth': '1993-02-22'},
    {'name': 'Michael Johnson', 'age': 35, 'location': 'Giza, Cairo, Egypt', 'gender': 'Male', 'date_of_birth': '1988-09-10'},
    {'name': 'Sophia Kim', 'age': 32, 'location': 'Gangnam, Seoul, South Korea', 'gender': 'Female', 'date_of_birth': '1991-11-30'},
    {'name': 'Mohammed Ali', 'age': 29, 'location': 'Bur Dubai, Dubai, UAE', 'gender': 'Male', 'date_of_birth': '1994-07-03'},
    {'name': 'laria Rodriguez', 'age': 31, 'location': 'Salamanca, Madrid, Spain', 'gender': 'Female', 'date_of_birth': '1990-03-17'},
    {'name': 'Yuki Tanaka', 'age': 27, 'location': 'Shinjuku, Tokyo, Japan', 'gender': 'Female', 'date_of_birth': '1995-01-25'},
    {'name': 'Ahmed Hassan', 'age': 34, 'location': 'Maadi, Cairo, Egypt', 'gender': 'Male', 'date_of_birth': '1989-08-05'},
    {'name': 'Carlos Martinez', 'age': 30, 'location': 'Chamartín, Madrid, Spain', 'gender': 'Male', 'date_of_birth': '1993-04-12'},
    {'name': 'James Brown', 'age': 38, 'location': 'Austin, Texas, USA', 'gender': 'Male', 'date_of_birth': '1983-12-05'},
    {'name': 'Emily Davis', 'age': 25, 'location': 'Los Angeles, California, USA', 'gender': 'Female', 'date_of_birth': '1996-09-02'},
    {'name': 'Carlos Gutierrez', 'age': 33, 'location': 'Monterrey, Mexico', 'gender': 'Male', 'date_of_birth': '1988-03-21'},
    {'name': 'Sofia Silva', 'age': 26, 'location': 'Sao Paulo, Brazil', 'gender': 'Female', 'date_of_birth': '1995-05-18'},
    {'name': 'Liam Murphy', 'age': 30, 'location': 'Dublin, Ireland', 'gender': 'Male', 'date_of_birth': '1991-07-14'},
]
# def get_max_difference_age(some_list: list):
#     max_difference = float('-inf')
#     pair = []
#     for i in range(len(some_list)):
#         for j in range(i + 1, len(some_list)):
#             if 'date_of_birth' in some_list[i] and 'date_of_birth' in some_list[j]:
#                 birtday_new1 = datetime.datetime.strptime(some_list[i]['date_of_birth'], '%Y-%m-%d')
#                 birtday_new2 = datetime.datetime.strptime(some_list[j]['date_of_birth'], '%Y-%m-%d')
#                 difference = round(abs((birtday_new1 - birtday_new2).days)/365, 2)
#                 if difference > max_difference:
#                     max_difference = difference
#                     pair = [some_list[i]['name'], some_list[j]['name']]
#     return pair, max_difference
# print(get_max_difference_age(people_list_new))


# 30. Подсчитайте, сколько людей живет в определенном районе (если места жительства содержат информацию о районе).
# def count_people_some_area(some_list: list):
#     dict_out = {}
#     counter = 0
#     region = None
#     for elem in some_list:
#
#         name = elem['name']
#         location = elem['location']
#         if ',' in location:
#             region = location.split(',')[1].strip()
#             if region not in dict_out:
#                 dict_out[region] = 1
#             else:
#                 dict_out[region] += 1
#     return dict_out
#
# print(count_people_some_area(people_list_new))

# 31. Найдите средний возраст людей с определенной первой буквой имени.
# def count_aver_age(some_list: list):
#     total = sum(elem['age'] for elem in some_list)
#     aver = round(total / len(some_list), 2)
#     return aver
# print(count_aver_age(people_list_new))
#
# def count_people_first_name(some_list: list, letter_first):
#     resalt_aver_age = count_aver_age(some_list)
#     counter = 0
#     for elem in some_list:
#         name_full = elem['name']
#         if name_full[0].lower().startswith(letter_first):
#            counter += 1
#     return counter
# print(count_people_first_name(people_list_new, letter_first='l'))

# 32. Создайте новый список, содержащий только людей с уникальными именами.
# def get_unique_name(some_list: list):
#     list_out = []
#     for elem in some_list:
#         name = elem['name'].split()
#         if name not in list_out:
#             list_out.append(name[0])
#     return list_out
# print(get_unique_name(people_list_new))

# 33. Найдите людей, родившихся в определенном году.
# import datetime
# def get_people_some_year(some_list: list, year_get):
#     people_list = []
#     for elem in some_list:
#         name = elem['name']
#         birthday = elem['date_of_birth']
#         birthday_new = datetime.datetime.strptime(birthday, '%Y-%m-%d')
#         if birthday_new.year == year_get:
#             people_list.append(name)
#     return people_list
# print(get_people_some_year(people_list_new, year_get=1988))

# 34. Создайте новый список, содержащий только мужчин/женщин.
# def get_list_people_gender(some_list: list):
#     men_list = []
#     women_list = []
#     for elem in some_list:
#         name = elem['name']
#         gender = elem['gender']
#         if gender == 'Male':
#             men_list.append(name)
#         else:
#             women_list.append(name)
#     return men_list, women_list
# print(get_list_people_gender(people_list_new))

# 35. Подсчитайте количество людей, у которых имена состоят из двух слов.
# def count_double_first_name(some_list: list):
#     counter = 0
#     for elem in some_list:
#         first_name = elem['name'].split()[0]
#         if len(first_name.split()) == 2:
#             counter += 1
#     return counter
#
# print(count_double_first_name(people_list_new))


# 36. Найдите человека с самым коротким именем.
# def get_shortest_name(some_list: list):
#     shortest_name = ''
#     shortest_name_length = float('inf')
#     for elem in some_list:
#         name = elem['name']
#         if len(name) < shortest_name_length:
#             shortest_name_length = len(name)
#             shortest_name = name
#         return shortest_name
# print(get_shortest_name(people_list_new))

# 37. Отсортируйте список по алфавиту сначала по месту жительства, а затем по имени.
# list_sort_location = sorted(people_list_new, key=lambda elem: (elem['location'], elem['name']))
# print(list_sort_location)

# 38. Подсчитайте количество людей, у которых возраст оканчивается на определенную цифру.
# def count_people(some_list: list, number_age:str):
#     counter = 0
#     for elem in some_list:
#         name = elem['name']
#         age = str(elem['age'])
#         if age.endswith(number_age):
#             counter += 1
#     return counter
# print(count_people(people_list_new, number_age='5'))

# 39. Найдите людей, чей возраст больше среднего возраста всех людей в списке.
# def count_aver_age(some_list: list):
#     total = sum(elem['age'] for elem in some_list)
#     aver = round(total / len(some_list), 2)
#     return aver
# print(count_aver_age(people_list_new))
#
# def get_people_older_aver_age(some_list: list):
#     list_out = []
#     resalt = count_aver_age(some_list)
#     for elem in some_list:
#         name = elem['name']
#         age = elem['age']
#         if age > resalt:
#             list_out.append(name)
#     return list_out
# print(get_people_older_aver_age(people_list))

# 40. Создайте новый список, содержащий только людей, у которых место жительства начинается на определенную букву.
# def get_some_people(some_list: list, letter_location):
#     list_out = []
#     for elem in some_list:
#         name = elem['name']
#         location = elem['location'].lower()
#         if location.startswith(letter_location):
#             list_out.append(name)
#     return list_out
# print(get_some_people(people_list_new, letter_location='s'))