"""class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_marks(self):
        return self.marks

    def set_marks(self, new_marks):
        if new_marks >= 0 and new_marks <= 100:
            self.marks = new_marks
            print("Marks updated successfully")
        else:
            print("Invalid marks. Enter marks between 0 to 100.")

    def show(self):
        print(f"Marks secured by {self.name} is {self.marks}")

s1 = Student("Imtiaz", 90)

print(s1.get_marks())
s1.set_marks(95)

print(s1.get_marks())"""

#Employee salary

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_salary(self):
        return self.salary

    def set_salary(self, new_salary):
        if new_salary >= 10000 and new_salary <= 200000:
            self.salary = new_salary
            print("Salary Updated")
        else:
            print("Invalid Salary")

    def show(self):
        print(f"{self.name}'s updated salary is {self.salary}")

emp1 = Employee("Imtiaz", 20000)
emp1.set_salary(25000)
emp1.show()
    


