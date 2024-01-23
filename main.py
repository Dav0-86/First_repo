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
