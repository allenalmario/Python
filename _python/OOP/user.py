class User():
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=2, balance=0)
    
    # adding the deposit method

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
    
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self
    
    def display_user_balance(self):
        print("Hello " + self.name.title() + " ")
        self.account.display_account_info()
        print("\n")
        return self

    def transfer_money(self, recipient, amount):
        self.make_withdrawal(amount)
        recipient.make_deposit(amount)
        self.display_user_balance()
        recipient.display_user_balance()
        return self

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
        return self

    def yield_interest(self):
        if self.balance < 0:
            print("Negative Balance!")
        else:
            self.balance += (self.balance * self.int_rate)
        return self

john = User("john", "john@web.com")
kate = User("kate", "kate@web.com")
brad = User("brad", "brad@web.com")

john.make_deposit(100).make_deposit(100).make_deposit(100).display_user_balance()

kate.make_deposit(1000).make_deposit(1000).make_withdrawal(100).make_withdrawal(100).make_withdrawal(100).display_user_balance()

brad.make_deposit(5000).make_withdrawal(200).make_withdrawal(200).make_withdrawal(200).display_user_balance().transfer_money(john, 500)