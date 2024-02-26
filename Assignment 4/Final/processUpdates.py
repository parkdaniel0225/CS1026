from country import Country
from catalogue import CountryCatalogue


def processUpdates(cntryFileName, updateFileName, BAD_UPDATE_FILE):
    oFile = open("output.txt", "w", encoding="utf-8")

    cntryFile = open(cntryFileName, "r")

    if cntryFile is None:

        while True:
            check = input("Do you want to Quit? 'Y' (yes) or 'N' (no): ")
            if check == "N":
                cntryFile = input("Enter a file name: ")
                file = open(cntryFileName, "r")
                if file is not None:
                    break

            if IOError:
                userInput = input("Country file name invalid. Do you want to Quit? 'Y' (yes) or 'N' (no): ")
                if userInput == "Y":
                    oFile.write("Update Unsuccessful\n")
                    oFile.close()
                    return False
                else:
                    cntryFile = input("Enter a file name: ")
                file = open(cntryFileName, "r")
                if file is not None:
                    break

            else:
                oFile.write("Update Unsuccessful\n")
                oFile.close()
                return False

    updateFile = open(updateFileName, "r")
    cCatalogue = CountryCatalogue(cntryFileName)

    for i in updateFile:

        i = i.strip()
        name = i.split(';')
        cntry = Country(name[0], '', '', '')
        country = cCatalogue.findCountry(cntry)

        if country is not None:
            for var in name[1:]:
                var = var.strip()
                if var[0] == 'P':
                    cCatalogue.setPopulationOfCountry(cntry, var[2:])
                elif var[0] == 'A':
                    cCatalogue.setAreaOfCountry(cntry, var[2:])
                elif var[0] == 'C':
                    cCatalogue.setContinentOfCountry(cntry, var[2:])
        else:
            for var in name[1:]:
                var = var.strip()
                if var[0] == 'P':
                    cntry.setPopulation(var[2:])
                elif var[0] == 'A':
                    cntry.setArea(var[2:])
                elif var[0] == 'C':
                    cntry.setContinent(var[2:])
            cCatalogue.addCountry(cntry.getName(), cntry.getPopulation(), cntry.getArea(), cntry.getContinent())

    cntryFile.close()
    cCatalogue.saveCountryCatalogue("output.txt")
    return True, cCatalogue
