class Student:  
    def __init__(self,name):  
        self.name = name
    def display (self):  
        print('The name of student is:',self.name)
 
first = Student('Cem') 
second = Student('Ece')
 
second.display()
