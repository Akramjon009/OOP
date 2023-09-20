class Reghtangel:
    def __init__(self, high, width):
        self.a = high
        self.b = width
    def getHigh(self):
        return self.a
    def salHigh(self, high):
        self.a = high
    def getWidth(self):
        return self.a
    def salWidth(self, width):
        self.b = width
    def getArea(self):
        return self.a * self.b
    def grtPerimetr(self):
        return (self.a + self.b)*2
    def getAll(self):
        return f'high : {self.a} width : {self.b} area : {self.getArea()} perimetr : {self.grtPerimetr()}'

r1 = Reghtangel(10, 9)
print(r1.getHigh())
r1.salHigh(12)
print(r1.getWidth())
r1.salWidth(34)
print(r1.getArea())
print(r1.grtPerimetr())
print(r1.getAll())