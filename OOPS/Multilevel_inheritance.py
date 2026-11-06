class Father:
    def __init__(self, num_heart):
        num_eyes = 2
        self.num_heart = num_heart
    def eat(self):
        print("I can eat")
    def cook(self):
        print("I can cook")
    def drive(self):
        print("I can drive")

class Son(Father):
    def __init__(self, name):
        self.name = name
    def Scooty(self):
        print("I have scooty")
    def laptop(self):
        print("I have laptop")
    def drive(self):
        print("I can drive")

class Grandson(Son):
    def __init__(self, heart, name, can_dance):
        Father.__init__(self,heart)
        Son.__init__(self,name)
        self.can_dance = can_dance
        
    def play(self):
        print("I can play")
    def swim(self):
        print("I can swim")
    def run(self):
        print("I can run")

child1 = Grandson(1, "Imtiaz", True)

print(child1.drive)