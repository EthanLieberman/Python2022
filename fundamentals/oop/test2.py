class test():
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height


    def show_height(self):
        print(self.height)



alex = test('alex',26,5)

alex.show_height()