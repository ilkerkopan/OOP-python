from employee import Employee

class HourlyEmployee(Employee):
    def __init__(self, name, lastname, ssn, hourly_wage, hours_worked):
        super().__init__(name, lastname, ssn)
        self.hourly_wage = hourly_wage
        self.hours_worked = hours_worked
        
    def calculate_earnings(self):
        if self.hours_worked < 40 :
            return self.hours_worked * self.hourly_wage
        else :
            return (40 * self.hourly_wage) + ((self.hours_worked-40)*1.5*self.hourly_wage)
        
    def get_info(self):
        return super().get_info() + "\nhourly wage: " + str(self.hourly_wage) + "\nhours worked: "+ str(self.hours_worked)
        