from Core import Core
from product import Burger, Basket, All, Sweets, Icecream
from os import system


class Display:

    def __init__(self) -> None:
        self.core = Core()
    def show(self):
        print(f'\tMenu')
        print(f'1. Burgerlar')
        print(f'2. Basketlar')
        print(f'3. Ichimliklar')
        print(f'4. Shirinliklar')
        print(f'5. Muzqaymoq')
        print(f'6.next')

    def choice(self):
        ch = int(input('>>> '))
        if ch == 1:
             new = Burger(input('Name: '), input('About: '), input('Cost: '))
             self.core.insert_burger(new.get_burger())

        elif ch == 2:
            new = Basket(input('Name: '), input('About: '), input('Cost: '))
            self.core.insert_basket(new.get_basket())

        elif ch == 3:
            new = All(input('Name: '), input('Cost: '))
            self.core.insert_drink(new.get_all())

        elif ch == 4:
            new = Sweets(input('Name: '), input('About: '), input('Cost: '))
            self.core.insert_sweets(new.get_sweets())
        elif ch == 5:
            new = Icecream(input('Name: '), input('About: '), input('Cost: '))
            self.core.insert_icecream(new.get_icecream())

    def remove(self):
        ch = int(input('>>> '))
        if ch == 1:
            self.core.remove_burger(input('enter burger '))

        elif ch == 2:
            self.core.remove_basket(input('enter basket '))

        elif ch == 3:
            self.core.remove_drinks(input('enter drinks '))

        elif ch == 4:
            self.core.remove_sweets(input('enter sweet '))
        elif ch == 5:
            self.core.remove_icecream(input('enter ice-cream '))


menu = Display()
menu.show()
menu.choice()
menu.show()