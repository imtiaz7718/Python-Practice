"""from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def area(self):
        length = 10 
        breadth = 5
        print("Rectangle area: ", length*breadth)

class Circle(Shape):
    def area(self):
        radius = 7
        print("Circle area: ", 3.14 * radius * radius)

rec = Rectangle()
rec.area()
cir = Circle()
cir.area()"""

from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class UPI(Payment):
    def pay(self, amount):
        print("Paid", amount, "using UPI")

class Card(Payment):
    def pay(Self, amount):
     print("Paid", amount, "using UPI")

upi = UPI()
card = Card()

upi.pay(5000)
    


        





    