class Animal():

    def __init__(self, name, species, size):
        self.name = name
        self.species = species
        self.size = size

    def printAnimal(self):
        print(self)

    def storeAnimalInFile(self, file_name):
        animal = str(self)
        with open(file_name, 'w+') as f:
            f.write(animal)
    
    def __str__(self):
        animal = ""
        animal += "Animal name: " + self.name + "\n"
        animal += "Animal species: " + self.species + "\n"
        animal += "Animal size: " + self.size + "\n"
        return animal