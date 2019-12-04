try: 
    age = int(input('Age: '))
    print(age)
except ValueError:
    print('Invalid value')

try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")