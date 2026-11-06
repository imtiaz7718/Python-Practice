from abc import ABC, abstractmethod

class TV(ABC):
    @abstractmethod
    def turn_on(self):
        pass

class Samsung(TV):
    def turn_on(self):
        print("Samsung TV is on")

class Haier(TV):
    def turn_on(self):
        print("Haier TV is on")

sn = Samsung()
sn.turn_on()
hr = Haier()
hr.turn_on()