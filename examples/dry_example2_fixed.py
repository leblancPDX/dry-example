class Animal():

    def __init__(self, name, species, size):
        self.name = name
        self.species = species
        self.size = size

    def printAnimal(self):
        print(self.serializeAnimal())

    def storeAnimalInFile(self, file_name):
        animal = self.serializeAnimal()
        with open(file_name, 'w+') as f:
            f.write(animal)
    
    def serializeAnimal(self):
        animal = ""
        animal += "Animal name: " + self.name + "\n"
        animal += "Animal species: " + self.species + "\n"
        animal += "Animal same: " + self.size + "\n"
        return animal