class Car:
    def __init__(self, name, price, capacity, color, model):
        self.__name = name
        self.__price = price
        self.__capacity = capacity
        self.__color = color
        self.__model = model
    def getName(self):
        return self.__name
    def getPrice(self):
        return self.__price
    def getCapacity(self):
        return self.__capacity
    def getColor(self):
        return self.__color
    def getModel(self):
        return self.__model
    def setname(self,name):
        self.__name = name
    def setprice(self,price):
        self.__price = price
    def setcapacity(self,capacity):
        self.__capacity = capacity
    def setcolor(self,color):
        self.__color = color
    def setmodel(self,model):
        self.__model = model
    def getAll(self):
        return f'{self.__name()} {self.__price} {self.__capacity} {self.__color} {self.__model}'
class Adress:
    def __init__(self, city, street, country):
        self.__city = city
        self.__street = street
        self.__country = country
    def __str__(self):
        return (f'''country: {self.__country}
city: {self.__city}
street: {self.__street}''')
    def getCity(self):
        return self.__city
    def getcountry(self):
        return self.__country
    def getStreet(self):
        return self.__street
    def setCity(self,city):
        self.__city = city
    def setstreet(self,street):
        self.__street = street
    def setcountry(self,country):
        self.__country = country
