class Market:
    def __init__(self, pro, balance, name, adres):
        self.products = pro
        self.balance = balance
        self.name = name
        self.adres = adres
    def getProd(self):
        return self.products.items()
    def addProd(self,newpronem,prace):
        self.products[newpronem] = prace
    def getBalance(self):
        return self.balance
    def removeProduct(self,new):
        del self.products[new]
    def addMony(self,mony):
        self.balance += mony
    def sell(self,prod,nums):
        m = self.products.keys()
        if prod in m:
            m = int(self.products[prod])
            self.balance += m*nums

n = {
    "Bread": 2800,
    "Apple": 4500,
    "Banana": 20000,
    "Butter": 45000,
    "Potato": 3000,
    "Tomato": 4500,
    "Water": 11000,
    "CocaCola": 16000,
    "Kaktus": 5000
}
user = Market(n, int(input('enter balance ')), input('enter name '),input('enter adres '))
while True:
    s = input('1.Get products  2.Add products\n3.Remove product  4.Add mony\n5.buoght 6.balance 7.end ')
    if s == '1':
        print(user.getProd())
    elif s == '2':
        user.addProd(input('enter product name '),int(input('enter price ')))
    elif s =='3':
        user.removeProduct(input('enter product name '))
    elif s == '4':
        user.addMony(input('enter mony '))
    elif s == '5':
        user.sell(input('enter product name '),int(input('how many ')))
    elif s == '6':
        print(user.getBalance())
    elif s == '7':
        break
    else:
        print('please enter right ')