from os import system
class Myday:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
        self.MONTH = ['Yanvar', 'Fevral', 'Mart', 'Aprel', 'May', 'Iyun', 'Iyul', 'Avgust', 'Sentabr', 'Oktabr','Noyabr', 'Dekabr']
        self.DAY_IN_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        self.DAY2_IN_MONTH = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    def isleapDate(self,year):
        if (year % 4 == 0 and year % 100) or year % 400 == 0:
            return True
        else:
            return False

    def __str__(self):
        if self.isleapDate(self.year):
            if self.day <= int(self.DAY2_IN_MONTH[self.month-1]):
                return f"{self.day}-{self.MONTH[self.month-1]} {self.year} yil"
            else:
                return 'False'
        else:
            if self.day <= int(self.DAY_IN_MONTH[self.month-1]):
                return f"{self.day}-{self.MONTH[self.month-1]} {self.year} yil"
            else:
                return 'False'
    def isvaliDate(self):
        if self.isleapDate(self.year):
            if 1 <= self.day <= int(self.DAY2_IN_MONTH[self.month-1]):
                return True
            else:
                return False
        else:
            if self.day <= int(self.DAY_IN_MONTH[self.month-1]):
                return True
            else:
                return False
    def setDate(self, day, month,year):
        if self.isleapDate(year):
            if day <= int(self.DAY2_IN_MONTH[month - 1]):
                self.day = day
                self.month = month
                self.year = year
            else:
                print('folse')
        else:
            if day <= int(self.DAY_IN_MONTH[month - 1]):
                self.day = day
                self.month = month
                self.year = year
            else:
                print('folse')
    def setDay(self, day):
        if day <= self.DAY2_IN_MONTH[self.month-1] and self.isleapDate(self.year):
            self.day = day
        elif day <= self.DAY_IN_MONTH[self.month-1] and not(self.isleapDate(self.year)):
            self.day = day

    def setMonth(self, month):
        if self.day <= self.DAY2_IN_MONTH[month - 1] and self.isleapDate(self.year):
            self.month = month
        elif self.day <= self.DAY_IN_MONTH[month - 1] and not (self.isleapDate(self.year)):
            self.month = month
    def setYear(self,year):
        if self.day <= self.DAY2_IN_MONTH[self.month - 1] and self.isleapDate(year):
            self.year = year
        elif self.day <= self.DAY_IN_MONTH[self.month - 1] and not (self.isleapDate(year)):
            self.year = year
    def getDay(self):
        return self.day
    def getMonth(self):
        return self.month
    def getYear(self):
        return self.year
    def nextDay(self):
        self.day += 1
        if self.isleapDate(self.year):
            if int(self.DAY2_IN_MONTH[self.month-1]) - self.day > 0:
                self.month += 1
                self.day = int(self.DAY2_IN_MONTH[self.month-1]) - self.day
                if self.month == 13:
                    self.month = 1
                    self.year += 1
            print('folse')
        else:
            if int(self.DAY_IN_MONTH[self.month-1]) - self.day > 0:
                self.month += 1
                self.day = int(self.DAY_IN_MONTH[self.month-1]) - self.day
                if self.month == 13:
                    self.month = 1
                    self.year += 1
            else:
                print('folse')
    def nextMonth(self):
        self.month += 1
        if self.isleapDate(self.year):
            if self.day <= self.DAY2_IN_MONTH[self.month-1]:
                if self.month == 13:
                    self.month = 1
                    self.year += 1
            else:
                print('folse')
        else:
            if self.day <= self.DAY_IN_MONTH[self.month-1]:
                if self.month == 13:
                    self.month = 1
                    self.year += 1
            else:
                print('folse')
    def nextYear(self):
        pass


day = int(input('sanani kiriting '))
month = int(input('oyni son korinishida kiriting '))
year = int(input('yilni kiriting '))
if 1 <= day and 1 <= month <= 12 and 1 <= year <= 9999:
    system('clear')
    a = Myday(day, month, year)
    print(a)
    while True:
        system('clear')
        n = input('1.change all 2.change day 3.change month 4.change year 5.get day 6.get month 7.get year 8.Next day 9.Next month 10.Next year 11.nothing')
        if n == '1':
            day = int(input('sanani kiriting '))
            month = int(input('oyni son korinishida kiriting '))
            year = int(input('yilni kiriting '))
            system('clear')
            if 1 <= day and 1 <= month <= 12 and 1 <= year <=9999:
                a.setDate(day, month, year)
            else:
                print('folse')
            print(a)
        elif n == '2':
            day = int(input('sanani kiriting '))
            system('clear')
            if 1 <= day:
                a.setDay(day)
            else:
                print('folse')
            print(a)
        elif n == '3':
            month = int(input('oyni son korinishida kiriting '))
            system('clear')
            if 1 <= month <= 12:
                a.setMonth(month)
            else:
                print('folse')
            print(a)
        elif n == '4':
            year = int(input('yilni kiriting '))
            system('clear')
            if 1 <= year <= 9999:
                a.setYear(year)
            else:
                print('folse')
            print(a)
        elif n == '5':
            print(a.getDay())
        elif n == '6':
            print(a.getMonth)
        elif n == '7':
            print(a.getYear())
        elif n == '8':
            a.nextDay()
            print(a)
        elif n == '9':
            a.nextMonth()
            print(a)
        elif n == '10':
            a.nextYear()
        elif n == '11':
            print('end')
            break
        system('clear')

    # print(d3.previousYear())
    # print(d3.previousMonth())
    # print(d3.previousDay())
else:
    system('clear')
    print('notogri kiritingiz ')