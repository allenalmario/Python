class BankAccount:
    def __init__(self, int_rate=1, balance=0):
        self.int_rate = int_rate / float(100)
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        self.balance -= amount
        return self
    
    def display_account_info(self):
        print("Balance: $" + str(self.balance))
        print("Interest Rate: " + str(self.int_rate))
        return self

    def yield_interest(self):
        if self.balance < 0:
            print("Negative Balance!")
        else:
            self.balance += (self.balance * self.int_rate)
        return self


bankAccount1 = BankAccount()
bankAccount2 = BankAccount(4, 200)

bankAccount1.deposit(1000).deposit(1000).deposit(1000).withdraw(100).yield_interest().display_account_info()
bankAccount2.deposit(3000).deposit(5000).withdraw(100).withdraw(100).withdraw(100).withdraw(100).display_account_info()