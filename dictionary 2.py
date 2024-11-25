# Создайте список городов с информацией о климате (температура, влажность) в разные сезоны.
# Напишите функцию для нахождения города с самыми приятными погодными условиями.
# cities_climate = [
#     {
#         'city': 'Нью-Йорк',
#         'seasons': {
#             'зима': {'температура': -1, 'влажность': 60},
#             'весна': {'температура': 12, 'влажность': 65},
#             'лето': {'температура': 28, 'влажность': 70},
#             'осень': {'температура': 16, 'влажность': 68}
#         }
#     },
#     {
#         'city': 'Лос-Анджелес',
#         'seasons': {
#             'зима': {'температура': 12, 'влажность': 75},
#             'весна': {'температура': 20, 'влажность': 70},
#             'лето': {'температура': 32, 'влажность': 65},
#             'осень': {'температура': 25, 'влажность': 72}
#         }
#     },
#     {
#         'city': 'Токио',
#         'seasons': {
#             'зима': {'температура': 5, 'влажность': 55},
#             'весна': {'температура': 15, 'влажность': 60},
#             'лето': {'температура': 28, 'влажность': 75},
#             'осень': {'температура': 20, 'влажность': 70}
#         }
#     }
# ]
# def get_data(my_list: list):
#     list_city = {}
#     list_out = []
#     for elem in my_list:
#         summa_temp = 0
#         summa_humidity = 0
#         city = elem['city']
#         seasons = elem['seasons']
#         for season_name, season_data in seasons.items():
#             temperature = season_data['температура']
#             humidity = season_data['влажность']
#             summa_temp += temperature
#             summa_humidity += humidity
#         aver_t = summa_temp / len(seasons)
#         aver_h = summa_humidity / len(seasons)
#         list_city[city] = (aver_t, aver_h)
#     best_temp = list(range(15, 22))
#     best_hum = list(range(60, 70))
#     for city, parameters in list_city.items():
#         if parameters[0] in best_temp and parameters[1] in best_hum:
#             list_out.append(city)
#     return list_out
# print(get_data(cities_climate))

