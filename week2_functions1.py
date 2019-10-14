def greet_user(username) :
    print(f"Hello {username}!")
    
greet_user("ilker")

def call_twice(f,name):
    f(name)
    f(name)

call_twice(greet_user,"ilker")