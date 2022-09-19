class Animal():

    def __init__(self, name, image, cost):
        self.name = name
        self.image = image
        self.cost = cost
    
    def buildAnimalDivString(self):
        html_output = "<div> \n"
        html_output += "  <p>" + self.name + "</p>\n"
        html_output += "  <img src=" + self.image + "/>\n"
        html_output += "  <p> Buy for $" + self.cost + "</p>\n"
        html_output = "</div>"


class Car():

    def __init__(self, name, image, cost):
        self.name = name
        self.image = image
        self.cost = cost
    
    def buildCarDivString(self):
        html_output = "<div> \n"
        html_output += "  <p>" + self.name + "</p>\n"
        html_output += "  <img src=" + self.image + "/>\n"
        html_output += "  <p> Buy for $" + self.cost + "</p>\n"
        html_output = "</div>"