class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says woof!")

dog1 = Dog("Rex", 3)
dog1.bark()

dog2 = Dog("Buddy", 5)
dog2.bark()

print(dog1.name)
print(dog2.name)


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

c1 = Circle(5)
print(c1.area())


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
r1 = Rectangle(4, 6)
print(r1.area())
print(r1.perimeter())