def greet_user(first_name, last_name) :
    print(f"Hello {first_name} {last_name}!")
    
greet_user("ilker", "Kopan")

def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name    
    return full_name.title()


student1 = get_formatted_name("halid", "dalkıran")
print(student1)
print(get_formatted_name("rıdvan", "kartal"))