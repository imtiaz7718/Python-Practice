# Method overloading means using the same method name with different parameter lists.
#Python doesn't support method overloading directly but similar behaviour can be achieved
#with default arguments and *args

"""class Calculator:
    def add(self, *args):
        return sum(args)

cal  = Calculator()
print(cal.add(10, 20, 30))
print(cal.add(10, 20, 30, 40))"""

# Employee salary calculation with or without bonus

"""class Employee:
    def __init__(self,name, basic, bonus = 0):
        self.name = name
        self.bonus = bonus
        self.basic = basic
    def salary_calculation(self):
        return self.basic + self.basic
    def show(self):
        return f"Salary for {self.name}, is {self.salary_calculation}"

emp1 = Employee("Imtiaz", 20000, 3000)
emp2 = Employee("Jana", 20000, 4000)
print(emp1.show())
print(emp2.show())"""

# Students marks calculation

"""class Student:
    def __init__(self, name, sub1, sub2, sub3):
        self.name = name
        self.sub1 = sub1 
        self.sub2 = sub2 
        self.sub3 = sub3
    def total(self, extra = 0):
        return self.sub1 + self.sub2 + self.sub3 + extra
    def show(self):
        return f"Total marks {self.name} secured is {self.total()}"

stud1 = Student("Imtiaz", 70, 65, 80)
stud2 = Student("Abdul", 80, 75, 55)
print(stud1.show())
print(stud2.show())"""

#Multiply

"""class Calculator:
    def __init(self, name):
        self.name = name

    def multiply(self, *numbers):
        result = 1
        for i in numbers:
            result *=i
        return result

c = Calculator("My Calculator")
print(c.multiply(10,20))
print(c.multiply(20,20))"""


"""class Vehicle:
    def __init__(self, name, price_per_day):
        self.name = name
        self.price_per_day = price_per_day
    def rent(self, days, insurance = 0):
        return (self.price_per_day * days) + insurance
    def show(self, days, insurance = 0):
        return f"The price of {self.name} for {days} days is, {self.rent(days, insurance)}"

v = Vehicle("car", 3000)
v1 = Vehicle("Bike", 1500)
print(v.show(3, 500))
print(v1.show(5))"""















