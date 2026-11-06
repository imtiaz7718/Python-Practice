#Protected
"""class Employee:
    def __init__(self, salary):
        self._salary = salary

class Manager(Employee):
    def display_salary(self):
        print("Salary: ", self._salary)

emp1 = Manager(40000)
emp1.display_salary()"""


#Private

"""class Parent:
    def __init__(self,amount):
        self.__amount = amount

class Child(Parent):
    def display(self):
        print(self.__amount)

c = Child()
c.display()"""   #it gives a attribute error

"""class Parent:
    def __init__(self,amount):
        self.__amount = amount
    def get_amount(self):
        return self.__amount

class Child(Parent):
    def show(self):
        print(self.get_amount())

ch = Child(5000)
ch.show()"""


class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited amount {amount}. New balance {self.__balance}")
        else:
            print("Invalid amount")

    def withdraw(self, amount):
            if amount <= 0:
                print("Invalid amount")
            elif self.__balance < amount:
                print("Insufficent balance")
            else:
                 self.__balance -= amount
                 print("Withdrawn amount {amount}. New balance {self.__balance}")

account1 = BankAccount(20000)
account2 = BankAccount(30000)
account1.withdraw(31000)
account2.deposit(0)
                 

        
        