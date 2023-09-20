class User:
    def __init__(self):
        self.name = input("Ismingiz nima? ")
        self.age = int(input("Yoshingiz nechida? "))
        self.balance = int(input("Balansingizda qancha pul bor? "))

    def getBalance(self):
        print(f"Sizning balansingizda {self.balance} UZS pul bor.")

    def addMoney(self):
        amount = int(input("Qancha pul qo'shmoqchisiz? "))
        self.balance += amount
        print(f"Sizning yangi balansingiz: {self.balance} UZS")

    def getMoney(self):
        amount = int(input("Qancha pul olmoqchisiz? "))
        if amount <= self.balance:
            self.balance -= amount
            print(f"Sizning yangi balansingiz: {self.balance} UZS")
        else:
            print("Kechirasiz, balansingizda yetarli mablag' yo'q.")

    def __str__(self):
        return f"Salom, mening ismim {self.name}, yoshim {self.age}da, lekin, shu yoshimda {self.balance} UZS pulim bor."


user = User()

while True:
    print("1.Add Money\n2.Get Money\n3.Get Balance\n4.Exit")
    choice = int(input("Tanlang: "))

    if choice == 1:
        user.addMoney()
    elif choice == 2:
        user.getMoney()
    elif choice == 3:
        user.getBalance()
    elif choice == 4:
        print("Dasturdan chiqildi.")
        break
    else:
        print("Noto'g'ri tanlov. Iltimos, qayta urinib ko'ring.")

    print(user)