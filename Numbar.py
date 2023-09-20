from datetime import date
class Number:
    def __init__(self, company, number, price):
        self.day = date.today()
        self.__company = company
        self.__number = number
        self.__price = price
