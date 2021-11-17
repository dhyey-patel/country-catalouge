##
#Dhyey Patel
#250960470
#December 6th 2017
#Assignment 4: Country Catalouge
##
# import the country class
from country import *
# initialize the country catalogue class
class CountryCatalogue:
    # constructor method that takes in the data file and continent file then makes a dictionary and a list with objects of the countyr class
    def __init__(self,cont,data):
        # open the 2 files
        dataFile = open(data,"r")
        contFile = open(cont,"r")
        # initialize the dictionary and the list that will be used throughout the class
        self._cDictionary = {}
        self._countryCat = []
        # go through the continent file and make the dictionary with each key being the country and the value being the continent
        for line in contFile:
            line = line.replace("\n","")
            contlist = line.split(",")
            if not(contlist[0]=="Country"):
                self._cDictionary[contlist[0]] = contlist[1]
        # go through the data file and make ojects of the class country and append it to the country catalogue list
        for line in dataFile:
            dataList = line.split("|")
            dataList[1] = dataList[1].replace(",","")
            dataList[2] = dataList[2].replace(",","")
            if not(dataList[0]=="Country"):
                country = Country(str(dataList[0]),int(dataList[1]),float(dataList[2]),str(self._cDictionary[dataList[0]]))
                self._countryCat.append(country)

    # method that finds a country from the country catalogue and returns that country as a country object
    def findCountry(self,c_name):
        for el in self._countryCat:
            if el.getName()==c_name:
                return el
        return None

    # method that changes the population of a country and return True/False depending on the success of the function
    def setPopulationOfCountry(self,c_name,pop):
        for el in self._countryCat:
            if el.getName()==c_name:
                el.setPopulation(pop)
                return True
        return False

    # method that changes the area of a country and return True/False depending on the success of the function
    def setAreaOfCountry(self,c_name,u_area):
        for el in self._countryCat:
            if el.getName()==c_name:
                el.setArea(u_area)
                return True
        return False

    # method that adds a country to the country catalogue and return True/False depending on the success of the function
    def addCountry(self,u_name,u_pop,u_area,u_cont):
        check = True
        for el in self._countryCat:
            if el.getName()==u_name:
                check = False
        if check:
            country = Country(u_name,u_pop,u_area,u_cont)
            self._countryCat.append(country)
            self._cDictionary[u_name]=u_cont
            return True
        else:
            return False

    #  method to delete the country from the country catalogue and the dictionary
    def deleteCountry(self,c_name):
        delete = -1
        for i in range(len(self._countryCat)):
            if self._countryCat[i].getName()==c_name:
                delete = i
        if delete!=-1:
            self._cDictionary.pop(self._countryCat[delete].getName())
            self._countryCat.pop(delete)

    # method that goes through the country catalogue and prints each element
    def printCountryCatalogue(self):
        for el in self._countryCat:
            print(el)

    # method returns a list of all the countries in a specific continent
    def getCountriesByContinent(self,cont):
        continentList=[]
        for el in self._countryCat:
            if el.getContinent()==cont:
                continentList.append(el)
        return continentList

    # method to return a list of tuples containing the country and the population in descending order
    def getCountriesByPopulation(self,cont="nothing"):
        populationList = []
        countryPopulationList={}
        countryPopulationListSorted=[]
        if cont == "nothing":
            for el in self._countryCat:
                countryPopulationList[el.getPopulation()] = el.getName()
                populationList.append(int(el.getPopulation()))
        else:
            continentList=[]
            for el in self._countryCat:
                if el.getContinent()==cont:
                    continentList.append(el)
            for el2 in continentList:
                countryPopulationList[el2.getPopulation()] = el2.getName()
                populationList.append(int(el2.getPopulation()))
        populationList = sorted(populationList,reverse=True)
        for pop in populationList:
            countryPopulation = (countryPopulationList[pop],pop)
            countryPopulationListSorted.append(countryPopulation)
        return countryPopulationListSorted

    # method to return a list of tuples containing the country and the area in descending order
    def getCountriesByArea(self,cont="nothing"):
        areaList = []
        countryAreaList={}
        countryAreaListSorted=[]
        if cont == "nothing":
            for el in self._countryCat:
                countryAreaList[el.getArea()] = el.getName()
                areaList.append(float(el.getArea()))
        else:
            continentList=[]
            for el in self._countryCat:
                if el.getContinent()==cont:
                    continentList.append(el)
            for el2 in continentList:
                countryAreaList[el2.getArea()] = el2.getName()
                areaList.append(float(el2.getArea()))
        areaList = sorted(areaList,reverse=True)
        for area in areaList:
            countryArea = (countryAreaList[area],area)
            countryAreaListSorted.append(countryArea)
        return countryAreaListSorted

    # finds the most populous continent and returns the continent and the population of the continent
    def findMostPopulousContinent(self):
        allContinents = set()
        continentPopulation = []
        continentPopulationSum={}
        for el in self._countryCat:
            allContinents.add(el.getContinent())
        for el2 in allContinents:
            continentPopulationList=[]
            for el3 in self._countryCat:
                if el2 == el3.getContinent():
                    continentPopulationList.append(el3.getPopulation())
            continentPopulationSum[sum(continentPopulationList)]=el2
            continentPopulation.append(sum(continentPopulationList))
        mostPopulous = max(continentPopulation)
        return (continentPopulationSum[mostPopulous],mostPopulous)

    # method that returns a list of all the countries and their population density that fall in the given range
    def filterCountriesByPopDensity(self,lb,ub):
        countryPopDensitySorted=[]
        allPopDensity = []
        countryPopDensity = {}
        for el in self._countryCat:
            popDensity = el.getPopDensity()
            if popDensity<=ub and popDensity>= lb:
                allPopDensity.append(popDensity)
                countryPopDensity[popDensity] = el.getName()
        allPopDensitySorted = sorted(allPopDensity,reverse=True)
        for el1 in allPopDensitySorted:
            countryPopDensitySorted.append((countryPopDensity[el1],el1))
        return countryPopDensitySorted

    # method that saves all the countries in the country catalogue to the given file with the given format
    def saveCountryCatalogue(self,outName):
        writeFile = open(outName,"w")
        countryNames = []
        countryCatSorted = []
        for country in self._countryCat:
            countryNames.append(country.getName())
        countryNames = sorted(countryNames)
        print(countryNames)
        for name in countryNames:
            for el2 in self._countryCat:
                if name == el2.getName():
                    countryCatSorted.append(el2)
        print(countryCatSorted)
        for el in countryCatSorted:
            writeText = el.getName()+"|"+el.getContinent()+"|"+str(el.getPopulation())+"|"+str(el.getArea())+"|"+str(el.getPopDensity())+"\n"
            writeFile.write(writeText)
        writeFile.close()
        readFile = open(outName,"r")
        check = 0
        counter = 0
        for line in readFile:
            el1 = countryCatSorted[counter]
            text = el1.getName()+"|"+el1.getContinent()+"|"+str(el1.getPopulation())+"|"+str(el1.getArea())+"|"+str(el1.getPopDensity())+"\n"
            if line == text:
                check+=1
            counter+=1
        if check == len(countryCatSorted):
            return check
        else:
            return -1
        readFile.close()

c1 = CountryCatalogue("continent.txt",'data.txt')
c1.saveCountryCatalogue('out1.txt')
