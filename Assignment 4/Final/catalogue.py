from country import Country


class CountryCatalogue:

    def __init__(self, countryFile):
        self.countryCat = {}
        self.cDictionary = {}
        self.file = open(countryFile, "r", encoding="utf-8")

        first_line = True
        for line in open(countryFile, "r", encoding="utf-8"):
            if first_line:
                first_line = False
                continue
            line = line.strip().replace(",", "").split("|")
            self.countryCat[line[0]] = Country(line[0], line[2], int(line[3]), line[1])
            self.file.close()

    def findCountry(self, country):
        if country.getName() in self.countryCat:
            return country
        else:
            return None

    def addCountry(self, country, population, area, continent):

        country = country.title()
        if country not in self.cDictionary.keys():

            continent = continent.title()
            self.cDictionary[country] = continent
            self.countryCat[country] = Country(country, population, area, continent)
            return True
        else:
            return False

    def saveCountryCatalogue(self, fname):
        oFile = open(fname, 'w', encoding="utf-8")

        countryList = []
        for country in self.countryCat.keys():
            countryList.append(country)
        countryList.sort()

        count = 0

        for country in countryList:
            countryName = self.countryCat[country].getName()
            population = self.countryCat[country].getPopulation()
            area = self.countryCat[country].getArea()
            continent = self.countryCat[country].getContinent()
            oFile.write("Country|Continent|Population|Area")
            oFile.write(countryName + '|' + continent + '|' + str(population) + '|' + str(area) + "\n")
            count += 1

        oFile.close()
        return count

    def printCountryCatalogue(self):
        for country in self.countryCat.keys():
            print(self.countryCat[country])

    def setPopulationOfCountry(self, country, pop):
        for _country in self.countryCat.keys():
            if _country == country.getName():
                self.countryCat[_country].setPopulation(pop + '\t')

    def setAreaOfCountry(self, country, area):
        for _country in self.countryCat.keys():
            if _country == country.getName():
                self.countryCat[_country].setArea(area + '\t')

    def setContinentOfCountry(self, country, continent):
        self.countryCat[country].setContinent(continent)

    def inCat(self, country):
        if country in self.countryCat.keys():
            return True
        else:
            return False
