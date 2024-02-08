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
