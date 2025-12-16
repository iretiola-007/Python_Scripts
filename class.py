class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def intro(self):
        print(f"{self.name} is {self.age} years old.")
        
name = input("Name? ")
age = input("Age? ")
        
person_1 = Person(name, age)
person_1.intro()

