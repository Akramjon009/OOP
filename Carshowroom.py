from Cars import Adress, Car
class Carshowroom:
    def __init__(self, adress: Adress = 0, cars: list = 0, name: str = 0, rating: list = 0):
        self.adress = adress
        self.cars = cars
        self.name = name
        self.rating = rating

#    - addCar(car: Car)= > car qo'shadi.
    def addCar(self, car: Car):
        car = str(car)
        with open('Cars.txt', 'a') as cars:
            print(car)
            cars.write(car+'\n')
#    - removeCar(car: Car)= > carni o 'chiradi
    def removeCar(self,car):
        for i in range(len(self.cars)):
            if car in self.cars[i]:
                del self.cars[i]
#    - getCarsInfo() = > Barcha carlarni print qiladi
    def getCar(self):
        with open('Cars.txt', 'r') as cars:
            return f'{cars.read()}'
    def setAdress(self,adress):
        self.adress = adress
#    - getAdress(): Adresni print qiladi
    def getAdress(self):
        return f'{self.adress}'
#    - changeName(newName): Avtasalon nomini almashtiradi
    def changeName(self,name):
        self.name = name
#    - getName(): Avtasalon nomini print qiladi.
    def getName(self):
        return self.name
#    - rate(rate: int): rating qo 'shadi(0<n<=5)
    def rate(self,rate):
        with open('raiting.txt', 'a') as reat:
            reat.write(str(rate))
#    - getAvarageRating(): o'ratacha ratingni chiqaradi.
    def getAvarageRating(self):
        with open('raiting.txt', 'r') as reat:
            self.rating = list(reat.read())
            m, n = type(sum(self.rating), type(len(self.rating)))
        return m, n
    def getAll(self):
        c = ''
        c +=f'''name: {self.name}
adress: {self.adress}'''
        with open('Cars.txt', 'r') as cars:
            self.cars = cars.read()
        for i in self.cars:
            c += str(i)
       # c += self.getAvarageRating()
        return c
