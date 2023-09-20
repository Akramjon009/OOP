from datetime import datetime
from Card import Card
from User import User
from os import system

class ATM:
    def __init__(self, name, cash, balans) -> None:
        self.name = name
        self.cash = cash
        self.balans = balans
        self.user = None

    def __choice(self):
        while self.user.card.getChanse() > 0:
            system('clear')
            print("1. Info")
            print("2. Get cash")
            print("3. Change password")
            print("4. put the many on the card")
            print("5. Exit")
            ch = int(input('>>> '))
            if ch == 1:
                print(self.user.card)
                time, date = self.get_now_time()
                print(f'Time: {time}\nDate: {date}')
            elif ch == 2:
                self.get_cash()
                print(self.user.card)
                time, date = self.get_now_time()
                print(f'Time: {time}\nDate: {date}')
            elif ch == 3:
                chanse = 3
                while chanse > 0:
                    psw = input('Password: ')
                    if psw == self.user.card.get_password():
                        new_psw = input('New password: ')
                        print(self.user.card.set_password(new_psw, psw))
                        chanse = 3
                        break
                    elif chanse > 1:
                        chanse -= 1
                        print('error password you have', chanse, 'chanse')
                    elif chanse == 1:
                        print('the last chanse ')
                        chanse -= 1
            elif ch == 4:
                self.get_creditCard()
                print(self.user.card)
                time, date = self.get_now_time()
                print(f'Time: {time}\nDate: {date}')
            elif ch == 5:
                break
            else:
                print('enter correct')
    def get_now_time(self):
        date = datetime.now()
        return datetime.strftime(date, f'%H:%M:%S'), datetime.strftime(date, f'%d-%m-%y')

    def enter_card(self, user: User):
        self.user = user
        chanse = 3
        while chanse > 0:
            pwd = input('Enter password: ')
            if user.card.get_password() == pwd:
                self.__choice()
                chanse = 3
                break
            elif chanse > 2:
                chanse -= 1
                print('error password you have', chanse , 'chanse')
            else:
                if chanse == 2:
                    print('the last chanse ')
                else:
                    print('you have exceeded your attempts because of this your card is frozen')
                chanse -= 1
        self.user.card.Chanse(chanse)
    def get_cash(self):
        summa = int(input('Enter summa: '))
        pnt = summa * 1.01
        if self.user.card.get_balans() >= pnt:
            self.balans += pnt
            self.cash -= summa
            self.user.card.minus_balans(pnt)
            self.user.add_cash(summa)

    def get_creditCard(self):
        summa = int(input('Enter summa: '))
        pnt = summa * 0.01
        if self.user.card.get_balans() >= pnt:
            self.balans -= summa - pnt
            self.cash += summa
            self.user.minus_cash(summa)
            self.user.card.add_balans(summa-pnt)

card1 = Card('Asaka', '8600111122223333', '05/25', 1000000)
user1 = User('John', "Doe", card1)
atm = ATM('SQB', 10000000, 600000)
atm.enter_card(user1)
if atm.user.card.getChanse() > 0:
    print(atm.user.card)
    print(atm.get_now_time())