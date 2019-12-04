first_number = "0"
second_number = "0"
try:
    answer = int(first_number) / int(second_number)
except ZeroDivisionError: 
    print("You can't divide by 0!")
else: 
    print(answer)
