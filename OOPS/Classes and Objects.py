"""class Employee:
    def __init__(self, name, salary):
        self.name = name 
        self.salary = salary
    def show(self):
        print(f"{self.name}'s salary is {self.salary}")


emp1 = Employee("Imtiaz", 50000)
emp2 = Employee("Prithivi", 60000)
emp3 = Employee("Akash", 70000)
emp3.show()"""

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount < 500:
            print("Invalid amount")
        else:
            self.balance += amount
            print(f"Hi {self.name},  Deposited amount {amount}. New balance {self.balance}")

    def withdraw(self, amount):
        if amount < 500:
            print("Less tha Rs.500 cannot be withdrawn")
        elif amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Hi {self.name}, Withdrawn amount {amount}. New balance {self.balance}")

account1 = BankAccount("Imtiaz", 20000)
account2 = BankAccount("Jana", 30000)
account3 = BankAccount("Akash", 40000)
account1.withdraw(30000)
account2.deposit(0)
account3.withdraw(35000)

        

        