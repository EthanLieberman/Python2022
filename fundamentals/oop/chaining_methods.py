class User:
    def __init__(self, name):
        self.name = name
        self.balance = 100


    def make_withdrawal(self, amount):
        self.balance -= amount
        return self

    def make_deposit(self, amount):
        self.balance += amount
        return self


    def display_user_balance(self):
        print(self.balance)


    def transfer_money(self, amount, user2):
        self.make_withdrawal(amount)
        user2.make_deposit(amount)
        print(self.balance)
        print(user2.balance)



jake = User('jake')
michelle = User('Michelle')
alex = User('Alex')

print('User Jake:')
jake.make_withdrawal(25).make_withdrawal(25).make_withdrawal(25).make_deposit(15).display_user_balance()


print('User Michelle:')
michelle.make_deposit(20).make_deposit(50).display_user_balance()


print('User Alex:')
alex.make_deposit(15).make_withdrawal(10).make_withdrawal(10).make_withdrawal(15).display_user_balance()

jake.transfer_money(1, alex)





