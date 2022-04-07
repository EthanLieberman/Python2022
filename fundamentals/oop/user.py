class user:
    def __init__(self, name):
        self.name = name
        self.balance = 100


    def make_withdrawal(self, amount):
        self.balance -= amount

    def make_deposit(self, amount):
        self.balance += amount


    def display_user_balance(self):
        print(self.balance)


    def transfer_money(self, amount, user2):
        self.make_withdrawal(amount)
        user2.make_deposit(amount)
        print(self.balance)
        print(user2.balance)



jake = user('jake')
michelle = user('Michelle')
alex = user('Alex')

print('User Jake:')
jake.make_withdrawal(25)
jake.make_withdrawal(25)
jake.make_withdrawal(25)
jake.make_deposit(15)

jake.display_user_balance()


print('User Michelle:')
michelle.make_deposit(20)
michelle.make_deposit(50)
michelle.display_user_balance()


print('User Alex:')
alex.make_deposit(15)
alex.make_withdrawal(10)
alex.make_withdrawal(10)
alex.make_withdrawal(15)
alex.display_user_balance()

jake.transfer_money(1, alex)





