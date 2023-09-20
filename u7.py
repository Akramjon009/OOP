from os import system as s
from u7class import User
user = User(input('enter name '),int(input('enter age ')),int(input('enter balance ')))
while True:
    n = input('''1.Add Money 2. GetMoney, 3. Get Balance 4.Exit nomli menyu chiqsin. ''')
    s('clear')
    if n == '1':
        user.addMony(int(input('how many many do want to add ')))
        s('clear')
    elif n == '2':
        user.gatMony(int(input('how many many do you want to get ')))
        s('clear')
    elif n == '3':
        print(user.gatBalance())
    elif n == '4':
        user.getAll()
        print(' End ')
        break
    else:
        print('please enter right ')
