# try:
#     result = 10 / 0
#     print(result)
# except ZeroDivisionError:
#     print("Cannot divide by zero")

# print("Program continues")

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Cannot divide by zero")
    except TypeError:
        print("Both values must be numbers")

print(divide(10, 2))
print(divide(10, 0))
print(divide(10, "x"))

try:
    f = open("test.txt", "r")
    content = f.read()
except FileNotFoundError:
    print("File not found")
finally:
    print("This always runs")