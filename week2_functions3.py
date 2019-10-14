def is_strong(password):
    upper_case_flag = False
    lower_case_flag = False
    digit_flag = False
    length_flag = False
    
    for char in password :
        if char.isupper() :
            upper_case_flag = True
        if char.islower() :
            lower_case_flag = True
        if char.isdigit() :
            digit_flag = True
    if len(password) >= 10 :
        length_flag = True
    
    is_strong = upper_case_flag and lower_case_flag and digit_flag and length_flag
    return is_strong

test_password = "1234567"
if (is_strong(test_password)) :
    print(f"{test_password} is strong")
else :
    print(f"{test_password} is weak")
    
