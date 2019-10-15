class Employee:
    no_emps = 0
    raise_amount = 1.04
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' +last+ '@company.com'
        Employee.no_emps +=1
    def fullname(self):
        return self.first + ' ' + self.last
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount )

print("number of emloyees: " + str(Employee.no_emps))
emp_1 = Employee('John','Son',60000)
print ("employee 1 pay:" + str(emp_1.pay))
emp_1.apply_raise()
print("employee 1 pay:" + str(emp_1.pay))
print("number of emloyees: " + str(Employee.no_emps))

emp_2 = Employee('Will', 'Smith', 10000)
print ("employee 2 pay:" + str(emp_2.pay))
emp_2.apply_raise()
print("employee 2 pay:" +str(emp_2.pay))
print("number of emloyees: " + str(Employee.no_emps))