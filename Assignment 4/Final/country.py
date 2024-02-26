class Country:
    def __init__(self, name, population, area, continent):
        self.name = name
        self.pop = population
        self.area = area
        self.continent = continent

    def getName(self):
        return self.name

    def getPopulation(self):
        return self.pop

    def getArea(self):
        return self.area

    def getContinent(self):
        return self.continent

    def setPopulation(self, population):
        self.pop = population

    def setArea(self, area):
        self.area = area

    def setContinent(self, continent):
        self.continent = continent

    def __repr__(self):
        classification = (self.name.title() + ' (pop: ' + str(self.pop).strip() + ', size: ' + str(self.area).strip() + ') in ' + self.continent.title())
        return classification
