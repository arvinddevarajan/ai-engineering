temperature = 23

if temperature > 30:
    print("It's hot")
else:
    print("It's not hot")
score = 75

if score >= 90:
    print("Grade: A")
elif score >= 75:
    print("Grade: B")
elif score >= 60:
    print("Grade: C")
else:
    print("Grade: F")

age = 20
has_id = True

if age >= 18 and has_id:
    print("Entry allowed")
else:
    print("Entry denied")


fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print(fruit)

for i in range(5):
    print(i)

for j in range(11):
    if j % 2 == 0:
        print(j)