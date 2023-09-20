class Acount():
    def __init__(self,id, name, balanc = 0):
        self.id = id
        self.name = name
        self.balanc = balanc
    def getId(self):
        return self.id
    def getName(self):
        return self.name
    def getBalance(self):
        return self.balanc
    def salCard(self,sum):
        self.balanc += sum
        return self.balanc
    def salDebit(self, sum2):
        if sum2 <= self.balanc:
            self.balanc -= sum2
        else:
            print('Amount exaded balnce')
        return self.balanc
    def transferTo(self,another,sum):
        if sum <= self.balanc:
            self.balanc -= sum
            another.balanc += sum
        else:
            print('Amount exaded balnce')
        return self.balanc, another
    def getAll(self):
        return f'id : {self.id} name : {self.name} balance : {self.balanc}\n'


people = Acount(15250, 'Akramjon', 5000)
people1 = Acount(15358, 'Qobiljon')
# print(people.getId())
# print(people.getName())
# print(people.getBalance())
# print(people.salCard(40))
# print(people.salDebit(70))
people.transferTo(people1, 900)
print(people.getAll(), people1.getAll())
