# # Створіть функцію get_days_from_today(date), яка розраховує кількість днів між заданою датою і поточною датою.

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








# # Вам необхідно написати функцію get_numbers_ticket(min, max, quantity), 
# # яка допоможе генерувати набір унікальних випадкових чисел для таких лотерей.

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
        if quant>=1 and quant<=diff:
            break
        else:
            print(f"You must enter the number of winning numbers between 1 and {diff}. Try again.")
    except ValueError:
        print("You entered incorrect data. Please enter an integer.")

def ticket_data_is_valid(min, max, quantity):
    return (1 <= min < max <= 1000) and (quantity <= max - min)

def get_numbers_ticket(min, max, quantity):
    lot = range(min, max)
    numbers = random.sample(lot, quantity)
    sorted_numbers = sorted(numbers)
    return sorted_numbers

if ticket_data_is_valid(minimal, maximal, quant):
    print(get_numbers_ticket(minimal, maximal, quant))
else:
    print("Ticket details are incorrect.")






# Функція, яка автоматично нормалізує номери телефонів до потрібного формату, 
# видаляючи всі зайві символи та додаючи міжнародний код країни, якщо потрібно.

import re

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

def normalize_phone(phone_number):
    phone_number = re.sub(r"[^\d+]", "", phone_number)
    return phone_number

def add_ua_code(code):       
    if code.startswith("+38"):
        return code
    elif code.startswith("8"):
        return "+3" + code
    elif code.startswith("38"):
        return "+" + code
    else:
        return "+38" + code

sanitized_numbers = [add_ua_code(normalize_phone(num)) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)





# Створити функцію get_upcoming_birthdays, яка допоможе вам визначати, кого з колег потрібно привітати з днем народження!


import datetime
from datetime import date
import calendar

users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Jay Lo", "birthday": "1986.01.25"},
    {"name": "Penelopa Crus", "birthday": "1989.01.29"}
]

def get_upcoming_birthdays(users=None):
    tday=datetime.datetime.today().date()
    birthdays=[]
    
    for user in users:
        bday = datetime.datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        bday = bday.replace(year=tday.year)
        
        if bday < tday:
            bday = bday.replace(year=tday.year + 1)
            
        day_of_week = calendar.day_name[bday.weekday()]
        
        if day_of_week == "Saturday":
            bday = bday + datetime.timedelta(days=2)
        elif day_of_week == "Sunday":
            bday = bday + datetime.timedelta(days=1)
        
        days_between=(bday-tday).days
        
        if 0<=days_between<7:
            birthdays.append({'name':user['name'], 'birthday':bday.strftime("%Y.%m.%d")}) 

    return birthdays
            
upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)