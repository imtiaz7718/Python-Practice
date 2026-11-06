"""class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __gt__(self, other):            #Dunder Methods gt - greater than, lt - lesser than
        if self.age > other.age:
            return True
        else:
            return False

p1 = Person("Imtiaz", 22)
p2 = Person("Jana", 23)

if p1 > p2:
    print(f"{p1.name} will pay the bill")
else:
    print(f"{p2.name} will pay the bill")"""

"""class Numbers:
    def __init__(self,value):
        self.value = value
    def __add__(self, other):
        return self.value + other.value


n1 = Numbers(10)
n2 = Numbers(20)
print(n1+n2)"""

"""class Numbers:
    def __init__(self, value):
        self.value = value
    def __sub__(self, other):
        return self.value - other.value

n1 = Numbers(20)
n2 = Numbers(10)
print(n1 - n2)"""

"""class Numbers:
    def __init__(self,value):
        self.value = value

    def __mul__(self, other):
        return self.value * other.value

n1 = Numbers(10)
n2 = Numbers(20)
print(n1 * n2)"""

"""class Complex:
    def __init__(self, real, imaginery):
        self.real = real
        self.imaginery = imaginery

    def __add__(self, other):
        return Complex(self.real + other.real, self.imaginery + other.imaginery)
    
    def show(self):
        print(f"{self.real} + {self.imaginery} i")

c1 = Complex(2, 3)
c2 = Complex(4, 5)
result = c1 + c2
result.show()"""


"""class Employee:
    def __init__(self, name, salary):
        self.name = name 
        self.salary = salary
    def __add__(self, other):
        return self.salary + other.salary
    def show(self, employees):
        total = self.salary
        names = [self.name]

        for i in employees:
            total += i.salary
            names.append(i.name)

        return f"Total Salaries of {', '.join(names)} is {total}"
        

emp1 = Employee("Imtiaz", 20000)
emp2 = Employee("Jana", 30000)
emp3 = Employee("Prithivi", 20000)
emp4 = Employee("Akash", 30000)
emp5 = Employee("Mani", 40000)

print(emp1.show([emp2, emp3, emp4, emp5]))"""

# Shopping cart program 

class Product:
    def __init__(self, name, price):
        self.name = name 
        self.price = price
    def __add__(self, other):
        return self.price + other.price
    def display(self, products):
        total = self.price
        names = [self.name] # we use list because we store multiple products
        for i in products:
            total += i.price
            names.append(i.name)
        print(f"Total price of {', '.join(names)} is {total}")

p1 = Product("Keyboard", 10000)
p2 = Product("Mouse", 5000)
p3 = Product("Laptop", 60000)
p2.display([p1, p3])

