from Cars import Car, Adress
from Carshowroom import Carshowroom
c = Carshowroom()
while True:
    n = input('1.add car 2.get adress 3.change name 4.get name 5.set adress 6.get avarage rating 7.All infarmation 8.end ')
    if n == '1':
        new = Car(input('enter name car '), input('enter price '), input('enter capicity '), input('enter color '), input('enter model '))
        c.addCar(new.getAll())
    elif n == '2':
        print(c.getAdress())
    elif n == '3':
        c.changeName(input('enter new name '))
    elif n == '4':
        print(c.getName())
    elif n == '5':
        new = Adress(input('enter city '), input('enter street '), input('enter country '))
        c.setAdress(new)
    elif n == '6':
        print(c.getAvarageRating())
    elif n == '7':
        print(c.getAll())
    elif n == '8':
        break
    else:
        print('enter karect ')
    while True:
        rating = int(input('enter rayting from 1 to 5 '))
        if 1 <= rating <= 5:
            c.rate(rating)
            break



