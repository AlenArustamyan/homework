#create a hierarchy of classes representing different types of bank accounts. Start
#with a base class called BankAccount. Then, create two subclasses,
#SavingsAccount and CheckingAccount. Each subclass should inherit from the
#BankAccount class.
#● The BankAccount class should have the following attributes and methods:
#○ Attributes: account_number, balance
#○ Methods: __init__ (constructor), deposit, withdraw, and get_balance
#● The SavingsAccount class should inherit from BankAccount and have an
#additional attribute interest_rate. Override the deposit method to add
#interest to the balance when a deposit is made.
# The CheckingAccount class should inherit from BankAccount and have an
#additional attribute overdraft_fee. Override the withdraw method to deduct
#the overdraft fee if a withdrawal causes the balance to go below zero.



class BankAccount:
    def __init__(self,acount_number,balance):
        self.acount_number = acount_number
        self.balance = balance
    def deposit(self, amount):
        self.balance = amount
    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print('Anbavarar Mijocner')
        return self.balance






class SavingAccount(BankAccount):
    def __init__(self,account_number,balance,interest_rate):
        super().__init__()