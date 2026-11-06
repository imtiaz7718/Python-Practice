# Duck typing means python cares about what an object can do, rathe than what type of object it is.

class Duck:
    def swim(self):
        print("Duck can swim")
    def speak(self):
        print("Quack Quack")

class Dog:
    def swim(self):
        print("DOG can swim")
    def speak(self):
        print("woof woof")

class Person:
    def swim(self):
        print("Person can swim")
    def speak(self):
        print("Blah Blah")

def display(obj):
    obj.swim()
    obj.speak()

d = Duck()
do = Dog()
Per = Person()
display(Per)