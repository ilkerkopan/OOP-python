#fibonacci calculator

def prin_all_fibonacci_numbers(n):
    fibonacci_number = [1,1]
    for i in range(2,n):
        sum_fibo = fibonacci_number[i-2] + fibonacci_number[i-1]
        fibonacci_number.append(sum_fibo)
        
    print(fibonacci_number)

def find_fibonacci(n):
    fibonacci_number = [1,1]
    for i in range(2,n):
        sum_fibo = fibonacci_number[i-2] + fibonacci_number[i-1]
        fibonacci_number.append(sum_fibo)
        
    return fibonacci_number[-1]