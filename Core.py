class Core:
    def insert_burger(self, burger):
        with open('burgers.txt', 'a') as file:
            file.write(burger+'\n')

    def insert_basket(self, basket):
        with open('baskets.txt', 'a') as file:
            file.write(basket+'\n')

    def insert_drink(self, drink):
        with open('drinks.txt', 'a') as file:
            file.write(drink+'\n')

    def insert_sweets(self, sweets):
        with open('sweet.txt', 'a') as file:
            file.write(sweets+'\n')

    def insert_icecream(self, icecream):
        with open('icecream.txt', 'a') as file:
            file.write(icecream+'\n')

    def remove_burger(self, d):
        with open('burgers.txt', 'r') as bur:
            lis = bur.readlines()
            lis = ' '.join(lis).split('\n')
            for i in range(len(lis)):
                lis[i] = lis[i].split('/')

        for i in range(len(lis)):
            if lis[i][0] == d:
                del lis[i]
                break
        with open('burgers.txt', 'w') as bur:
            for i in lis:
                if i != ['']:
                    bur.write(f'{i}\n')

    def remove_basket(self, d):
        with open('baskets.txt', 'r') as bur:
            lis = bur.readlines()
            lis = ' '.join(lis).split('\n')
            for i in range(len(lis)):
                lis[i] = lis[i].split('/')

        for i in range(len(lis)):
            if lis[i][0] == d:
                del lis[i]
                break
        with open('baskets.txt', 'w') as bur:
            for i in lis:
                if i != ['']:
                    bur.write(f'{i}\n')

    def remove_drinks(self, d):
        with open('drinks.txt', 'r') as bur:
            lis = bur.readlines()
            lis = ' '.join(lis).split('\n')
            for i in range(len(lis)):
                lis[i] = lis[i].split('/')

        for i in range(len(lis)):
            if lis[i][0] == d:
                del lis[i]
                break
        with open('drinks.txt', 'w') as bur:
            for i in lis:
                if i != ['']:
                    bur.write(f'{i}\n')

    def remove_sweets(self, d):
        with open('sweets.txt', 'r') as bur:
            lis = bur.readlines()
            lis = ' '.join(lis).split('\n')
            for i in range(len(lis)):
                lis[i] = lis[i].split('/')

        for i in range(len(lis)):
            if lis[i][0] == d:
                del lis[i]
                break
        with open('sweets.txt', 'w') as bur:
            for i in lis:
                if i != ['']:
                    bur.write(f'{i}\n')

    def remove_icecream(self, d):
        with open('icecream.txt', 'r') as bur:
            lis = bur.readlines()
            lis = ' '.join(lis).split('\n')
            for i in range(len(lis)):
                lis[i] = lis[i].split('/')

        for i in range(len(lis)):
            if lis[i][0] == d:
                del lis[i]
                break
        with open('icecream.txt', 'w') as bur:
            for i in lis:
                if i != ['']:
                    bur.write(f'{i}\n')
























































































































































