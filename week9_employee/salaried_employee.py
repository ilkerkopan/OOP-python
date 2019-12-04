from employee import Employee

class SalariedEmployee(Employee):
    def __init__(self, name, lastname, ssn, weekly_salary):
        super().__init__(name, lastname, ssn)
        self.weekly_salary = weekly_salary
        
    def calculate_earnings(self):
        return self.weekly_salary
    
    def get_info(self):
        return super().get_info() + "\nweekly salary: " + self.weekly_salary
        
