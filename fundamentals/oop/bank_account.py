class BankAccount:
    def __init__(self, int_rate=.01, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient funds: Charging a $5 fee")
            self.balance - 5
        else:
            self.balance -= amount

        return self

    def display_acount_info(self):
        print(self.balance)

        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance + (self.balance * self.int_rate)
        return self

    def allInfo(self):
        print(self.balance)
        print(self.int_rate)




account1=BankAccount(.01, 100)

account2=BankAccount(.03, 200)


account1.deposit(20).deposit(20).deposit(20).withdraw(15).yield_interest().display_acount_info()


account2.deposit(10).deposit(10).withdraw(5).withdraw(5).withdraw(5).withdraw(5).yield_interest().display_acount_info()


account1.allInfo()