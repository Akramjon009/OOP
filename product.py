class All:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost
    def get_all(self):
        return f'''{self.name}/{self.cost}'''
class Burger(All):
    def __init__(self, name, about, cost) -> None:
        super().__init__(name, cost)
        self.about = about
    def get_burger(self) -> str:
        return f'''{super().get_all()}/{self.about}'''


class Basket(All):
    def __init__(self, name, about, cost) -> None:
        super().__init__(name, cost)
        self.about = about

    def get_basket(self) -> str:
        return f'''{super().get_all()}/{self.about}'''

class Icecream(All):
    def __init__(self, name, cost, about) -> None:
        super().__init__(name, cost)
        self.about = about
    def get_icecream(self) -> str:
        return f'''{super().get_all()}/{self.about}'''

class Sweets(All):
    def __init__(self, name, cost, about) -> None:
        super().__init__(name, cost)
        self.about = about

    def get_sweets(self) -> str:
        return f'''{super().get_all()}/{self.about}'''