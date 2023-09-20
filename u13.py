from datetime import date
from Numbar import Number
class Company:
    def __init__(self, companyName):
        self.companyName = companyName
        self.establ = date.today()
        self.__phonenumber = []
        self.__buget = 0
    def getphonenumber(self):
        return self.__phonenumber
    def getbuget(self):
        return self.__buget
    def setphonenumber(self,phonenumber):
        self.__phonenumber = phonenumber
    def setbuget(self,bughet):
        self.__buget = bughet
    def addNumber(self,number:Number):
        self.__phonenumber.append(number)
    def sellNumber(self,number):
        if number in self.__phonenumber:
            self.setbuget += number.getPrice
            self.__phonenumber.remove(number)

    def __str__(self) -> str:
        return f''''''
