def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
        func()
    return wrapper

@my_decorator
def say_whee():
    t = 1
    print("Whee!")
    print(t)

say_whee1 = my_decorator(say_whee)
#print(say_whee)
#say_whee1()
say_whee()