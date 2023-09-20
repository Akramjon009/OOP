from company import Company
from number import Number
from os import system
from time import sleep

while True:
    companys = input('''\033[1;34menter Ucell or Beeline or Uzmobile or MobiUz or stop
>>> ''')
    number2 = Number()
    system('clear')
    if companys == 'Ucell' or companys == 'Beeline' or companys == 'Uzmobile' or companys == 'MobiUz' or companys == 'stop':
        if companys != 'stop':
            companyFile = open(companys+".txt", "r")
            companyNumbers = companyFile.readlines()

            co = Company(companyName=companys)
            price = 1000
            for i in companyNumbers:
                price += 100
                co.addNumber(number=Number(company=co, number=i, price=price))
            compPhoneNumbers = co.getPhoneNumbers()
            number = input('enter number ')
            b = -1
            a = 0
            for i in companyNumbers:
                b += 1
                with open(companys+'soldnumber.txt', 'r') as soldenumber:
                    n = soldenumber.read()
                if not number in n:
                    a = '1'
                    if i[5:-1].join('') == number.join(''):
                        a = True
                        with open(companys+'soldnumber.txt', 'a') as soldenumber:
                            soldenumber.write(number+'\n')
                        print('price', co.number2.getPrice(), 'sum')
                        n = input('''if do want to buy this number enter yes else no 
>>> ''')
                        if n.lower() =='yes':
                            co.sellNumber(compPhoneNumbers[b])
                            print(co)
                        break
            if a == 0:
                print('this number has olready been sold ')
            elif a == '1':
                print('error')
        elif companys == 'stop':
            print('end')
    sleep(5)
    system('clear')