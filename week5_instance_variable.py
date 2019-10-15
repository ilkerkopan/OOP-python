class Employee:
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
    def apply_raise(self):
        self.pay = int(self.pay * 1.04)

emp_1 = Employee('John','Son',60000)
print ("employee 1 pay:" + str(emp_1.pay))
emp_1.apply_raise()
print("employee 1 pay:" + str(emp_1.pay))

emp_2 = Employee('Will', 'Smith', 10000)
print ("employee 2 pay:" + str(emp_2.pay))
emp_2.apply_raise()
print("employee 2 pay:" +str(emp_2.pay))