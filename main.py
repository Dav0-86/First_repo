import datetime


date1 = input("Введіть дату у форматі yyyy-mm-dd: ")

try:
    date_input = datetime.datetime.strptime(date1, "%Y-%m-%d")

except Exception:
    print("Помилка: дата має бути у форматі yyyy-mm-dd")


def get_days_from_today(date):
    date_now = datetime.datetime.today()
    if date <= date_now:
        difference_time = date_now - date_input
    else:
        difference_time = -(date_input - date_now)
    return difference_time.days
    
print(get_days_from_today(date_input))