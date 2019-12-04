from comission_employee import ComissionEmployee
from salaried_employee import SalariedEmployee
from hourly_employee import HourlyEmployee
from base_plus_comission_employee import BasePlusComissionEmployee

employees = []
employees.append(SalariedEmployee("ilker", "Kopan", "1234", "1000"))
employees.append(HourlyEmployee("Ozan", "Arslan", "2623",hourly_wage=30, hours_worked=45))
employees.append(ComissionEmployee("Elif", "Akyar", "2406", gross_sale=5000, comission_rate=0.1))
employees.append(BasePlusComissionEmployee("Emre", "Uluçam", "3519", gross_sale=5000, comission_rate=0.03, base_salary=1000))

for employee in employees:
    print("-"*20)
    print(employee.get_info())
    print("calculated earning for this week : " + str(employee.calculate_earnings()))