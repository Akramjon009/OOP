class Men:
    def __init__(self,id, fname, lname, salary):
        self.id = id
        self.fname = fname
        self.lname = lname
        self.salary = salary
    def getId(self):
        return self.id
    def getFname(self):
        return self.fname
    def getLname(self):
        return self.lname
    def saleFullname(self):
        return f'{self.fname} {self.lname}'
    def gatSalary(self):
        return self.salary
    def gat1yaerSalary(self):
        return self.salary*12
    def salaryinporsent(self,persent):
        self.salary += self.salary * (persent/100)
    def tostring(self):
        return f'id : {self.id} Fullname : {self.saleFullname()} salary : {self.salary}'

akramjon=Men( 15250, 'Akramjon', 'Abduvahobov', 300)
print(akramjon.getId())
print(akramjon.getFname())
print(akramjon.getLname())
print(akramjon.saleFullname())
print(akramjon.gatSalary())
print(akramjon.gat1yaerSalary())
akramjon.salaryinporsent(15)
print(akramjon.tostring())
