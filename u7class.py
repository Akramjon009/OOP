class User:
    def __init__(self, name, age, balance):
        self.name = name
        self.age = age
        self.balance = balance
    def gatBalance(self):
        return self.balance
    def addMony(self,mony):
        self.balance += mony
    def gatMony(self, mony):
        if mony <= self.balance:
            self.balance -= mony
        else:
            print('Amount exaded balnce')
    def getAll(self):
        print(f'name : {self.name} age : {self.age} balance : {self.balance}')
