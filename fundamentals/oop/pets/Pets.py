class Pet():
    def __init__(self, name, kind, tricks, health, energy):
        self.name = name
        self.kind = kind
        self.tricks = tricks
        self.health = health
        self.energy = energy

    def sleep(self):
        print("pet sleeps")

    def eat(self, food):
        print("pet eats", food)

    def play(self):
        print("pet run in the grass")

    def noise(self):
        print("pet makes some noises")
