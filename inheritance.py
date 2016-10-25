class Pet(object):
    name =""
    species = ""
    def __init__(self, name, species):
        self.name = name
        self.species = species


class Dog(Pet):
    breed = ""
    def __init__(self, name, breed):
        Pet.__init__(self, name, "Dog")
        self.breed = breed

pet = Pet("Mister Bird", "bird")
dog = Dog("Missi", "Buhund")
print isinstance(pet, Pet), isinstance(pet, Dog), isinstance(dog, Pet), isinstance(dog, Dog)
