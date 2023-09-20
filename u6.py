class Time:
    def __init__(self, sek, min, h):
        self.sek = sek
        self.min = min
        self.h = h
    def getSek(self):
        return self.sek
    def getMin(self):
        return self.min
    def getHour(self):
        return self.h
    def salSek(self,newsek):
        self.sek = newsek
    def salMin(self,newmin):
        self.min = newmin
    def salHour(self,newh):
        self.h = newh
    def getTime(self):
        print(f'seconds :{self.sek}   minutes : {self.min}   hour : {self.h}')
    def getAll(self):
        if self.sek > 59:
            self.min += self.sek // 60
            self.sek = self.sek % 60
        if self.min > 59:
            self.h += self.min // 60
            self.min = self.min % 60
        if self.h > 23:
            self.h = self.h % 24
        print('%02d:%02d:%02d' % (self.h, self.min, self.sek))
    def getAll1(self):
        self.sek += 1
        if self.sek > 59:
            self.min += self.sek // 60
            self.sek = self.sek % 60
        if self.min > 59:
            self.h += self.min // 60
            self.min = self.min % 60
        if self.h > 23:
            self.h = self.h % 24
        print('%02d:%02d:%02d' % (self.h, self.min, self.sek))
    def getAll2(self):
        self.sek -= 1
        print('%02d:%02d:%02d' % (self.h, self.min, self.sek))

times = Time(230, 59, 59)
print(times.getSek())
print(times.getMin())
print(times.getHour())
times.salSek(696)
times.salMin(660)
times.salHour(240)
times.getTime()
times.getAll()
times.getAll1()
times.getAll2()
