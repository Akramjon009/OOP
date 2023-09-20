from datetime import date
from number import Number
class Company:
    def __init__(self, companyName):
        self.companyName = companyName
        self.establishedAt = date.today()
        self.__phoneNumbers = []
        self.__budget = 0

    def getcompany(self):
        return self.companyName
    def setBudget(self, money):
        self.__budget = money

    def getBudget(self):
        return self.__budget
    
    def setPhoneNumbers(self, numbers):
        self.__phoneNumbers = numbers
    
    def getPhoneNumbers(self):
        return self.__phoneNumbers
    
    def addNumber(self, number: Number):
        self.__phoneNumbers.append(number)

    def sellNumber(self, number: Number):
        if number in self.__phoneNumbers:
            self.__phoneNumbers.remove(number)
            self.__budget += number.getPrice()

    def __str__(self) -> str:
        return f"{self.companyName} has been established at {self.establishedAt} and today it has {len(self.__phoneNumbers)} numbers and budget ${self.__budget}"


    
