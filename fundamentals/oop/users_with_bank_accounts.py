class user:
    def __init__(self, name):
        self.name = name
        self.account = {'checking': BankAccount(), 'savings' : BankAccount()}


    def make_withdrawal(self, amount, acc1):
        self.account.withdraw(amount, acc1)
        return self

    def make_deposit(self, amount, acc):
        self.account[acc].deposit(amount)
        return self


    def display_user_balance(self, acc):
        # print(self.name,self.account,sep='****', end='_')
        self.account[acc].display_acount_info()


    def transfer_money(self, amount, acc1, user2, acc2):
        self.account[acc1].withdraw(amount)
        user2.account[acc2].deposit(amount)
        self.display_user_balance()
        user2.display_user_balance()




class BankAccount:
    def __init__(self, int_rate=.01, balance=100):
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





user2 = user("jack")

user2.account['newacc'] = BankAccount()
user2.display_user_balance('newacc')
user1 = user("adam")

user1.make_deposit(200, 'checking').display_user_balance('checking')
user1.make_deposit(350, 'savings').display_user_balance('savings')
user2.display_user_balance('savings')

# user1.transfer_money(50,'checking', user2, 'savings')