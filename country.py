##
#Dhyey Patel
#250960470
#December 6th 2017
#Assignment 4: Country Catalouge
##
# initialize country class
class Country:
    # constructor method which takes in name, population, area, and continent
    def __init__(self,u_name,u_pop,u_area,u_cont):
        self._name = u_name
        self._population = u_pop
        self._area = u_area
        self._continent = u_cont
    # method to return country's name
    def getName(self):
        return self._name
    # method to return country's population
    def getPopulation(self):
        return self._population
    # method to return country's area
    def getArea(self):
        return self._area
    # method to return continent of the country
    def getContinent(self):
        return self._continent
    # method to set country's population
    def setPopulation(self,u_pop):
        self._population = u_pop
    # method to set country's area
    def setArea(self,u_area):
        self._area = u_area
    # method to set continent of the country
    def setContinent(self,u_cont):
        self._continent = u_cont
    #method to find populaiton density and return it
    def getPopDensity(self):
        self._popDensity = (self._population/self._area)
        self._popDensity = round(self._popDensity,2)
        return self._popDensity
    # method to change  the display to the given format
    def __repr__(self):
        return self._name+"(pop: "+str(self._population)+", size: "+str(self._area)+") in "+ str(self._continent)
