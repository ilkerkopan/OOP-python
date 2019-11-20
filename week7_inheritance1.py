class Person:
    def __init__(self, name, birthyear):
        self.name = name
        self.birthyear = birthyear
        
    def eat(self):
        print(f'{self.name} is eating')
        
    def sleep(self):
        print(f'{self.name} is sleeping')
        
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name
        
    def set_birthyear(self, birthyear):
        self.birthyear = birthyear
    
    def get_birthyear(self):
        return birthyear
    
    def get_info(self):
        return 'Name: '+self.name.title()+' birthyear: '+str(self.birthyear)
    
class Worker(Person):
    def __init__(self, name, birthyear, salary):
        super().__init__(name, birthyear)
        self.salary = salary
    
    def work(self, hour=None):
        if hour == None:
            print(f'{self.name} working')
        else:
            print(f'{self.name} working for {hour} hours')
            
    def get_salary(self):
        return self.salary
    
    def set_salary(self, salary):
        self.salary = salary
       
    def get_info(self):
        return super().get_info() + ' salary: '+str(self.salary)
    
worker1 = Worker("ilker Kopan", 1981, 1000)
worker1.eat()
worker1.work()
worker1.work(6)
print(worker1.get_salary())
print(worker1.get_info())

person1 = Person("Ali", 2001)
print(person1.get_info())