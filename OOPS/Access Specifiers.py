"""class BankAccount:
    def __init__(self):
        self.name = "Imtiaz"
        self._balance = 5000 #_ protected __ private
        self.__pin = 1234

    def show_balance(self):
        print(self._balance)

account = BankAccount()
print(account.name)
print(account._balance)
print(account.show_balance())"""

"""class Calculator:
    def __init__(self):
        self.__secret_number = 10
    def __display_secret(self):           #private style method
        print(self.__secret_number)
    def show(self):
        self.__display_secret()

cal = Calculator()
cal.show()"""  # it works because it is public, cal.__display_secret raises an error

"""class Person:
    def __init__(self):
        self.name = "Imtiaz"
        self._age = 22
        self.__password = "abc123"

    def show_password(self):
        print(self.__password)

person = Person()
print(person.name)
print(person._age)
#person.show_password()
print(person.__password)""" #raises an error because it is private, we should declare it inside the class


class Student:
    def __init__(self, name, rollno, age):
        self.name = name
        self._rollno = rollno
        self.__age = age
    def __display(self):
        print(f"Hi myself {self.name}, {self.__age} and the Roll Number is {self._rollno}")
    def displayprivate(self):
        self.__display() 
class Branch(Student):
    def show(self):
        print(f"My roll no is {self._rollno}")

s1 = Student("Imtiaz", 15, 22)
print(s1._Student__age) #Name Mangling, we can access the private variable with this
s1._Student__display()
