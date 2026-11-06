class ElectricityBill:
    def __init__(self, name, units):
        self.name = name 
        self.units = units

    def calculate_bill(self, fixed_charges = 0):
        if self.units <= 200:
             return 0
        elif self.units >= 201 and self.units <= 400:   
         bill = self.units * 4.70
         return bill + fixed_charges
        elif self.units >= 401 and self.units <= 500:   
          bill = self.units * 4.70
          return bill + fixed_charges
        elif self.units >= 501 and self.units <= 600:   
                  bill = self.units * 4.70
                  return bill + fixed_charges
        elif self.units >= 601 and self.units <= 800:   
                  bill = self.units * 4.70
                  return bill + fixed_charges
        elif self.units >= 801 and self.units <= 1000:   
                  bill = self.units * 4.70
                  return bill + fixed_charges
        else:
             bill = self.units * 11.55
             return bill + fixed_charges
    def show(self, fixed_charges = 0):
        return f"Hi {self.name}, your electricity bill for this month is {self.calculate_bill(fixed_charges)}"


bill1 = ElectricityBill("Imtiaz", 10000) #Attributes __init
bill2 = ElectricityBill("Jana", 150)
print(bill1.show())
print(bill2.show(100)) #Methods 