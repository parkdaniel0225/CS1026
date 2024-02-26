class Country:

    name = "Null_Space"
    population = "0"
    area = "0"
    continent = "Null_Place"

    def __init__(self, name, continent, pop, area):
        self.name = name
        self.population = pop
        self.area = area
        self.continent = continent

    def getName(self):
        return self.name

    def getPopulation(self):
        return self.population

    def getArea(self):
        return self.area

    def getContinent(self):
        return self.continent

    def setPopulation(self, pop):
        self.population = pop

    def setArea(self, area):
        self.area = area

    def setContinent(self, continent):
        self.continent = continent

    def __repr__(self):
        return f"{self.name} (pop: {self.population}, size: {self.area}) in {self.continent} \n"

