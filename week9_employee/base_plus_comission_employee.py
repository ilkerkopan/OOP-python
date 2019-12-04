from comission_employee import ComissionEmployee

class BasePlusComissionEmployee(ComissionEmployee):
    def __init__(self, name, lastname, ssn, gross_sale, comission_rate, base_salary):
        super().__init__(name, lastname, ssn, gross_sale, comission_rate)
        self.base_salary = base_salary
        
    def calculate_earnings(self):
        return super().calculate_earnings() + self.base_salary
        
    def get_info(self):
        return super().get_info() + "\nbase salary : " + str(self.base_salary)
        

