class Data:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.yaer = year
    def getDay(self):
        return self.day
    def getMonth(self):
        return self.month
    def getYear(self):
        return self.yaer
    def salDay(self,newday):
        self.day = newday
    def salMonth(self,newmonth):
        self.month = newmonth
    def salYear(self,newyear):
        self.yaer = newyear
    def getAll(self):
        print(f'{self.day} {self.month} {self.yaer}')
    def getAll2(self):
        print('%02d/%02d/%02d' % (self.day, self.month, self.yaer))
data = Data(15,4,2008)
print(data.getDay())
print(data.getMonth())
print(data.getYear())
data.salDay(14)
data.salMonth(3)
data.salYear(2009)
data.getAll()
data.getAll2()
