def greet():
    print("Hello from a function")

greet()

def greet_name(name):
    print(f"Hello, {name}")

greet_name("Alice")
greet_name("Bob")

def add(a, b):
    return a + b

result = add(3, 5)
print(result)

def power(base, exponent=2):
    return base ** exponent

print(power(3))
print(power(3, 3))

def is_even(num):
    if num % 2 == 0:
        return True 
    else:
        return False
    
print(is_even(4))
print(is_even(7))
