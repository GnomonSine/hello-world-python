# @Author: Farhad Yusifov
# @Email: farhadyusifov@protonmail.com
# @Date: 2025-08-28

# @Description: An example of classes.

class Mammal():
    def walk(self):
        return print("walk")


class Dog(Mammal):
    species = "Canis familiaris"

    def __init__(self, name, age, tricks=["bark"]):
        self.name = name
        self.age = age
        self.tricks = tricks
    
    def bark(self):
        return print(f"{self.name} says {self.tricks[0]}!")


Maxy = Dog("Maxy", 3)
Maxy.bark()
