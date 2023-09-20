from datetime import datetime

date = datetime.now()

print(datetime.strftime(date, f'%H:%M:%S %d/%m/%y'))