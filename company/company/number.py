from datetime import date


class Number:
    def __init__(self, company, number, price) -> None:
        self.createdAt = date.today()
        self.__company = company
        self.__number = number
        self.__price = price

    def setCompanyName(self, name):
        self.__company = name

    def getCompanyName(self):
        return self.__company

    def setNumber(self, number):
        self.__number = number
    
    def getNumber(self):
        return self.__number

    def setPrice(self, price):
        self.__price = price
    
    def getPrice(self):
        return self.__price
    
    def __str__(self) -> str:
        return f"Number: {self.__number}\nCompany is: {self.__company} and price is {self.__price}"
