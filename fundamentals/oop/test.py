class testParent:
    def __init__(self, t, w, bal):
        self.test = t
        self.we = w
        self.balance = bal

    def mytest(self):
        pass


    @classmethod
    def tax(cls, amount):
        return cls(4, 2, amount - 15)
# return testparent(4,2, 50 - 15)
# return testparent(4,2,35)


user1 = testParent(1,3,20)

print(user1.balance)

user2 = testParent.tax(50)
# user2 = testparent(4,2,35)

print(user2.balance)


arr = [2,3,6,3]