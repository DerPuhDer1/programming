#1. polymorphism
#2. Inheritence
#3. Encapsulation
import datetime
class Automobile():
    #Define a constructor
    #The constructor defines what happens when we create a automobile
    def __init__(self, make, model, vin, engine_size, owner, year):
        #Assign parameter values
        self.__make = make
        self.__model = model
        self.__vin = vin
        self.__engine_size = engine_size
        self.__owner = owner
        self.__year = year

    #create getter and setter methods for class attributes
    def get_make(self):
        return self.__make
    
    def get_model(self):
        return self.__model
    
    def get_vin(self):
        return self.__vin
    
    def get_engine_size(self):
        return self.__engine_size
    
    def set_engine_size(self, new_size):
        self.__engine_size = new_size

    def get_owner(self):
        return self.__owner
    
    def set_owner(self, new_owner):
        self.__owner = new_owner

    def get_year(self):
        return self.__year
    
    #get automobile age
    def get_age(self):
        #get the current year
        the_date = datetime.datetime.now()
        this_year = the_date.year

        #Return the difference between the current year and auto year as the age
        return this_year - self.__year

    #Create a method to print automobile data
    def print_data(self):
        print(f"{self.__year} {self.__make} {self.__model}")
        print(f"VIN: {self.__vin}, Engine size: {self.__engine_size}")
        print(f"Owner: {self.__owner}\n")