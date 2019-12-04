from employee import Employee

class ComissionEmployee(Employee):
    def __init__(self, name, lastname, ssn, gross_sale, comission_rate):
        super().__init__(name, lastname, ssn)
        if gross_sale < 0 :
            raise Exception("Gross sale must be greater than 0")
        self.gross_sale = gross_sale
        if comission_rate < 0 :
            raise Exception("Comission rate must be greater than 0")
        self.comission_rate = comission_rate
        
    def calculate_earnings(self):
        return self.comission_rate * self.gross_sale - (self.gross_sale * 0.01)
        
    def get_info(self):
        return super().get_info() + "\ngross sale : " + str(self.gross_sale) + "\ncomission rate: "+ str(self.comission_rate)
        
