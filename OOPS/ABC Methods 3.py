"""from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def Payment(self, amount):
        pass

class UPI(Payment):
    def Payment(self, amount):
        print("Paid amount using UPI: ", amount)

class Cash(Payment):
    def Payment(self, amount):
        print("Paid amount using cash: ", amount)

class Card(Payment):
    def Payment(self, amount):
        print("Paid amount using card: ", amount)

upi = UPI()
cash = Cash()
card = Card()

upi.Payment(1000)"""

"""from abc import ABC, abstractmethod

class Mobile(ABC):
    @abstractmethod
    def call(self):
        pass

class Samsang(Mobile):
    def call(self):
        print("Calling from Samsung")
    def show(self):
        print("This is my Mobile")

s1 = Samsang()
s1.call()
s1.show()"""

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def stop(self):
        pass

class Bike(Vehicle):
    def start(self):
        print("Bike is started")
    def stop(self):
        print("Bike is stopped")

class Scooty(Vehicle):
    def start(self):
        print("Scooty is started")
    def stop(self):
        print("Scooty is stopped")


b1 = Bike()
b1.start()
b1.stop()
s1 = Scooty()
s1.start()
s1.stop()


