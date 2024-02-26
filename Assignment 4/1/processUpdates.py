from country import Country
from catalogue import CountryCatalogue


def processUpdates(cntryFileName, updateFileName, badUpdateFile):

    # open output file
    outputFile = open("output.txt", "w", encoding="utf-8")

    # testing for valid country file
    W = False
    while W == False:
        try:
            countryFile = open(cntryFileName, "r", encoding="utf-8")
            W = True
        except IOError:
            userInput = input("Country file name invalid. Do you wish to QUIT? ")
            if userInput == "N":
                 cntryFileName = input("Enter new file name: ")
            else:
                outputFile.write("Update Unsuccessful\n")
                return (False, None)

    # testing for update file
    W = False
    while W == False:
        try:
            updateFile = open(updateFileName, "r", encoding="utf-8")
            W = True
        except IOError:
            userInput = input("Update file name invalid. Do you wish to QUIT? ")
            if userInput == "N":
                 updateFileName = input("Enter new file name: ")
            else:
                outputFile.write("Update Unsuccessful\n")
                return (False, None)

    # Create new catalogue from the country file
    catalogue = CountryCatalogue(cntryFileName)
    # list of continents for later
    continents = ["Africa", "Antarctica", "Arctic", "Asia", "Europe", "North_America", "South_America"]

    # read the first line from the update file
    nextLine = updateFile.readline()

    # while loop to iterate the update file
    while nextLine != "":
        # temporary list to store the line of updates
        tempList = nextLine.split(";")

        # strip spaces and remove blank lines
        i = 0
        while i < len(tempList):
            tempList[i] = tempList[i].strip()
            if "" in tempList:
                tempList.remove("")
            i += 1

        # checking to see if the country is inside the catalogue or if the list has an invalid length
        if catalogue.inCat(tempList[0]) and len(tempList) <= 4:

            # variables to check for duplicated updates
            popUpdate = False
            areaUpdate = False
            contUpdate = False
            dupes = False

            if len(tempList) >= 2:
                # checking for duplicate updates
                update = tempList[1].split("=")
                if update[0] == "P":
                    popUpdate = True
                elif update[0] == "A":
                    areaUpdate = True
                elif update[0] == "C" and update[1] in continents:
                    contUpdate = True
            elif len(tempList) >= 3:
                update = tempList[2].split("=")
                if update[0] == "P" and popUpdate == False:
                    popUpdate = True
                elif update[0] == "A" and areaUpdate == False:
                    areaUpdate = True
                elif update[0] == "C" and update[1] in continents and contUpdate == False:
                    contUpdate = True
                else:
                    outputFile.write("Duplicate updates found in second section.\n")
                    return(False, catalogue)
            elif len(tempList) >= 4 and dupes != True:
                update = tempList[3].split("=")
                if update[0] == "P" and popUpdate == False:
                    popUpdate = True
                elif update[0] == "A" and areaUpdate == False:
                    areaUpdate = True
                elif update[0] == "C" and update[1] in continents and contUpdate == False:
                    contUpdate = True
                else:
                    outputFile.write("Duplicate updates found in third section.\n")
                    return(False, catalogue)


            if len(tempList) >= 2 and dupes != True:
                # checking the first update for info
                update = tempList[1].split("=")
                if update[0] == "P":
                    catalogue.setPopulationOfCountry(tempList[0], update[1])
                elif update[0] == "A":
                    catalogue.setAreaOfCountry(tempList[0], update[1])
                elif update[0] == "C" and update[1] in continents:
                    catalogue.setContinentOfCountry(tempList[0], update[1])

            if len(tempList) >= 3 and dupes != True:
                update = tempList[2].split("=")
                if update[0] == "P":
                    catalogue.setPopulationOfCountry(tempList[0], update[1])
                elif update[0] == "A":
                    catalogue.setAreaOfCountry(tempList[0], update[1])
                elif update[0] == "C" and update[1] in continents:
                    catalogue.setContinentOfCountry(tempList[0], update[1])

            if len(tempList) >= 4 and dupes != True:

                update = tempList[3].split("=")

                if update[0] == "P":
                    catalogue.setPopulationOfCountry(tempList[0], update[1])
                elif update[0] == "A":
                    catalogue.setAreaOfCountry(tempList[0], update[1])
                elif update[0] == "C" and update[1] in continents:
                    catalogue.setContinentOfCountry(tempList[0], update[1])

        elif catalogue.inCat(tempList[0]) != True:
            catalogue.addCountry(tempList[0], tempList[1].split("=")[1], tempList[2].split("=")[1], tempList[3].split("=")[1])

            if len(tempList) >= 2:
                # checking the first update for info
                update = tempList[1].split("=")
                if update[0] == "P":
                    catalogue.setPopulationOfCountry(tempList[0], update[1])
                elif update[0] == "A":
                    catalogue.setAreaOfCountry(tempList[0], update[1])
                elif update[0] == "C" and update[1] in continents:
                    catalogue.setContinentOfCountry(tempList[0], update[1])

            if len(tempList) >= 3:
                update = tempList[2].split("=")
                if update[0] == "P":
                    catalogue.setPopulationOfCountry(tempList[0], update[1])
                elif update[0] == "A":
                    catalogue.setAreaOfCountry(tempList[0], update[1])
                elif update[0] == "C" and update[1] in continents:
                    catalogue.setContinentOfCountry(tempList[0], update[1])

            if len(tempList) >= 4:

                update = tempList[3].split("=")

                if update[0] == "P":
                    catalogue.setPopulationOfCountry(tempList[0], update[1])
                elif update[0] == "A":
                    catalogue.setAreaOfCountry(tempList[0], update[1])
                elif update[0] == "C" and update[1] in continents:
                    catalogue.setContinentOfCountry(tempList[0], update[1])
        nextLine = updateFile.readline()

    # write all data to output file
    catalogue.saveCountryCatalogue("output.txt")
    return(True, catalogue)
