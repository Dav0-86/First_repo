import datetime


date1 = input("Enter the date in the format yyyy-mm-dd: ")
now = datetime.datetime.today()
date1_now = now.strftime("%Y-%m-%d")
while True:
    try:
        date_input = datetime.datetime.strptime(date1, "%Y-%m-%d")
        break

    except ValueError:
        print("The date must be in the format yyyy-mm-dd")
        date1 = input("Enter the date in the format yyyy-mm-dd: ")




def get_days_from_today(date):
    date_now = datetime.datetime.today()
    if date <= date_now:
        difference_time = date_now - date_input
    else:
        difference_time = -(date_input - date_now)
    return difference_time.days
    
print(f" The difference of days between {date1} and {date1_now} is equal {get_days_from_today(date_input)} day(s).")





import random

while True:
    try:
        minimal = int(input("Enter the minimum draw number: "))
        if minimal >= 1 and minimal <= 999:
            break
        else:
            print("You must enter data between 1 and 999. Try again.")
    except ValueError:
        print("You entered incorrect data. Please enter an integer.")
        
while True:
    try:
        maximal = int(input("Enter the maximum draw number: "))
        if 2<=maximal<=1000 and maximal>minimal:
            break 
        else:
            print(f"You must enter a maximum draw number between 2 and 1000." 
              f"The maximum number must be greater than {minimal}. Try again.")        
    except ValueError:
        print("You entered incorrect data. Please enter an integer.")         
        
        
        
while True:
    try:
        quant = int(input("Enter the number of winning numbers: "))
        diff=int(maximal-minimal)
        if quant>1 and quant<=diff:
            break
        else:
            print(f"You must enter the number of winning numbers between 1 and {diff}. Try again.")
    except ValueError:
        print("You entered incorrect data. Please enter an integer.")


def get_numbers_ticket(min, max, quantity):
    lot = range(min, max)
    quanty = random.sample(lot, quantity)
    sort_quanty = sorted(quanty) 
    return sort_quanty
print(get_numbers_ticket(minimal, maximal, quant))
