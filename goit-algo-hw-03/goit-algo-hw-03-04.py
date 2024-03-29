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
        congratulation_date = bday
        
        if day_of_week == "Saturday":
            congratulation_date = bday + datetime.timedelta(days=2)
        elif day_of_week == "Sunday":
            congratulation_date = bday + datetime.timedelta(days=1)
        
        days_between=(bday-tday).days
        congratulation_date_between=(congratulation_date-tday).days
        if 0<=days_between<7:
            birthdays.append({'name':user['name'], 'birthday':bday.strftime("%Y.%m.%d")}) 
        elif 0<=congratulation_date_between<7:
            birthdays.append({'name':user['name'], 'birthday':bday.strftime("%Y.%m.%d")})

    return birthdays
            
upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
