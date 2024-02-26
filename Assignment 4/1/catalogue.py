from country import Country

class CountryCatalogue:
    countryCat = {}


    def __init__(self, countryFile):
            countryFile = open(countryFile, "r", encoding="utf-8")
            nextLine = countryFile.readline()
            while nextLine != "":
                tempList = (nextLine.split("|"))
                self.countryCat[tempList[0]] = (Country(tempList[0], tempList[1], tempList[2], tempList[3]))
                nextLine = countryFile.readline()

    def setPopulationOfCountry(self, country, pop):
        self.countryCat[country].setPopulation(pop)

    def setAreaOfCountry(self, country, area):
        self.countryCat[country].setArea(area + "\n")

    def setContinentOfCountry(self, country, continent):
        self.countryCat[country].setContinent(continent)

    def findCountry(self, country):
        if country.getName() in self.countryCat:
            return country
        else:
            return None
    def inCat(self, country):
        if country in self.countryCat.keys():
            return True
        else:
            return False

    def addCountry(self, countryName, pop, area, cont):
        self.countryCat[countryName] = Country(countryName, cont, pop, area)

    def printCountryCatalogue(self):
        return f"{self.countryCat}"

    def saveCountryCatalogue(self, fname):
        outputFile = open(fname, "w", encoding="utf-8")
        tempList = []
        for key in self.countryCat:
            tempList.append(key)
        tempList.sort()

        outputFile.write("Country|Continent|Population|Area\n")
        for key in tempList:
            outputFile.write(self.countryCat[key].getName() + "|" + self.countryCat[key].getContinent() + "|" + self.countryCat[key].getPopulation() + "|" + self.countryCat[key].getArea())




