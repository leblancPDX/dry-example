class MarketplaceObject():

    def __init__(self, name, image, cost):
        self.name = name
        self.image = image
        self.cost = cost
    
    def buildMarketplaceObjectDivString(self):
        html_output = "<div> \n"
        html_output += "  <p>" + self.name + "</p>\n"
        html_output += "  <p>" + self.getClassification() + "</p>\n"
        html_output += "  <img src=" + self.image + "/>\n"
        html_output += "  <p> Buy for $" + self.cost + "</p>\n"
        html_output = "</div>"


class Animal(MarketplaceObject):

    def __init__(self, name, image, cost, breed):
        MarketplaceObject.__init__(self, name, image, cost)
        self.breed = breed
    
    def getClassification(self):
        return self.breed


class Car(MarketplaceObject):

    def __init__(self, name, image, cost, make, model):
        MarketplaceObject.__init__(self, name, image, cost)
        self.make = make
        self.model = model
    
    def getClassification(self):
        return self.make + " " + self.model