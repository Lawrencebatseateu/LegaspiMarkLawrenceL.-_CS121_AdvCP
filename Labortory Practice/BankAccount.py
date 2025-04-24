from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, account_number, balance=0):
        self._account_number = account_number
        self._balance = balance

    @property
    def account_number(self):
        return self._account_number

    @property
    def balance(self):
        return self._balance

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def show_account_type(self):
        pass

class CurrentAccount(BankAccount):
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    def withdraw(self, amount):
        if self._balance - amount >= -5000:
            self._balance -= amount

    def show_account_type(self):
        return "Current Account"

class SavingsAccount(BankAccount):
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount

    def show_account_type(self):
        return "Savings Account"

def print_account_details(account):
    print(f"Account Number: {account.account_number}")
    print(f"Balance: {account.balance}")
    print(f"Type: {account.show_account_type()}")
    print("----------------------------------")

acc1 = SavingsAccount("SA123", 1200)
acc2 = SavingsAccount("SA571", 1000)
acc3 = CurrentAccount("CA456", 500)
acc4 = CurrentAccount("CA625", 1000)

acc1.deposit(0)
acc1.withdraw(0)

acc2.withdraw(1100)

acc3.withdraw(700)
acc4.withdraw(7000)

print_account_details(acc1)
print_account_details(acc2)
print_account_details(acc3)
print_account_details(acc4)