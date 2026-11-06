class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance= balance
    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"Hi {self.name} deposited amount is {amount}. New balance is {self.balance}")
    def withdraw(self, amount):
            if self.balance < amount:
                 print("Insufficient Funds")
            else:
               self.balance = self.balance + amount
               print(f"Hi {self.name} deposited amount is {amount}. New balance is {self.balance}")
        
account1 = BankAccount("Imtiaz", 10000)
account2 = BankAccount("Jana", 20000)
account1.deposit(10000)