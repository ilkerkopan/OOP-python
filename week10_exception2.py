try: 
    age = int(input('Age: '))
    score = 100 / age
    print(age)
except ValueError:
    print('Invalid value')
except ZeroDivisionError:
    print('Invalid age')
