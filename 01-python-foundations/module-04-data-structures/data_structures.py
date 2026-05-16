fruits = ["apple", "banana", "mango"]

print(fruits)
print(fruits[0])
print(fruits[-1])
print(len(fruits))

fruits.append("grape")
print(fruits)

fruits.remove("banana")
print(fruits)

person = {
    "name": "Alice",
    "age": 30,
    "role": "engineer"
}

print(person["name"])
print(person["age"])

person["city"] = "New York"
person["age"] = 31

print(person)


for key, value in person.items():
    print(f"{key}: {value}")

coordinates = (10, 20)

print(coordinates)
print(coordinates[0])

#coordinates[0] = 99

#challenge

dictionary = {
    "model": "Tesla Model S",
    "temperature": 75,
    "max_tokens": 2048
}

for key, value in dictionary.items():
    print(f"{key}: {value}")