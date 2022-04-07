class ninja():
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        # self.pets = {}
        self.pet = pet
        self.treat = treats
        self.pet_food = pet_food

    def walk(self):
        print(f'{self.first_name} walks {self.pet.name}')
        

    def feed(self):
        self.pet.eat(self.treat)
        

    def bath(self):
        print(f'{self.first_name} washes {self.pet.name}')

    
    # def add_pet(self, name, kind, tricks, health, energy):
    #     self.pets[name] = Pet(name, kind, tricks, health, energy)

    # def change_pet_name(self, pet, new_name):
    #     self.pets[pet].name = new_name
    #     self.pets[new_name] = self.pets.pop(pet)