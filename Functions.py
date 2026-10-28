import random
class BankAccount:
    balance = 0
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.account_number = random.randint(10000000, 99999999)

    def deposit(self, amount):
        amount = float(input(f"\nHow much would you like to deposit? "))
        self.balance += amount

    def withdraw(self, amount):
        amount = float(input(f"\nHow much would you like to withdraw? "))
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount

    def account_information(self):
        return f"\nAccount Holder: {self.name}\nAccount Number: {self.account_number}\nBalance: ${self.balance:,.2f}"

    def quit(self):
        print("\nThank you for using Carter's Bank.")
        exit()

