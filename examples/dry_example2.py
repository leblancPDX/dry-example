class Animal():

    def __init__(self, name, species, size):
        self.name = name
        self.species = species
        self.size = size

    def printAnimal(self):
        print("Animal name: " + self.name)
        print("Animal species: " + self.species)
        print("Animal same: " + self.size)

    def storeAnimalInFile(self, file_name):
        animal = ""
        animal += "Animal name: " + self.name + "\n"
        animal += "Animal species: " + self.species + "\n"
        animal += "Animal same: " + self.size + "\n"
        with open(file_name, 'w+') as f:
            f.write(animal)