class Cercle:
    def __init__(self, radius, color):
        self.r = radius
        self.color = color
    def getRadius(self):
        return self.r
    def setRadius(self,radius):
        self.r = radius
    def getColor(self):
        return self.color
    def setColor(self,color):
         self.color = color
    def getArea(self):
        return (self.r**2) * 3.14
    def getCercle(self):
        return self.r*3.14*2
    def getAll(self):
        return f'''radius : {self.r} color : {self.color} area : {self.getArea()} fullinfo : {self.getCercle()}'''
c1 = Cercle(3,'red')
print(c1.getRadius())
c1.setRadius(4)
print(c1.getColor())
c1.setColor('blue')
print(c1.getArea())
print(c1.getCercle())
print(c1.getAll())
