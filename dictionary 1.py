# Создайте список компаний с информацией о сотрудниках и их зарплатах.
# Напишите функцию для нахождения компании с самой высокой средней зарплатой.
# companies = [
#     {
#         'name': 'Company A',
#         'employees': [
#             {'name': 'John Doe', 'salary': 50000},
#             {'name': 'Jane Doe', 'salary': 55000},
#             {'name': 'Jim Brown', 'salary': 60000}
#         ]
#     },
#     {
#         'name': 'Company B',
#         'employees': [
#             {'name': 'Bob Smith', 'salary': 48000},
#             {'name': 'Sue Johnson', 'salary': 52000},
#             {'name': 'Tom Davis', 'salary': 58000}
#         ]
#     }
# ]
# def find_company_with_highest_average_salary(companies_list):
#     highest_average_salary = 0
#     company_with_highest_salary = None
#
#     for company in companies_list:
#         company_name = company['name']
#         employees = company['employees']
#
#         total_salary = sum(employee['salary'] for employee in employees)
#         average_salary = total_salary / len(employees)
#
#         if average_salary > highest_average_salary:
#             highest_average_salary = average_salary
#             company_with_highest_salary = company_name
#
#     return company_with_highest_salary
#
# highest_salary_company = find_company_with_highest_average_salary(companies)
# print(f"Компания с самой высокой средней зарплатой: {highest_salary_company}")

