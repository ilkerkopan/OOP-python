from abc import ABC,abstractmethod

class Employee(ABC):
    def __init__(self, name, lastname, ssn):
        self.name = name
        self.lastname = lastname
        self.ssn = ssn
    
    @abstractmethod
    def calculate_earnings(self):
        pass
    
    def get_info(self):
        return self.name + " " + self.lastname + "\nsocial security number: " + self.ssn