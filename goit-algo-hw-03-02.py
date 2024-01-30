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

