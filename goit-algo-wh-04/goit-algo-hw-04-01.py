
text = '''Alex Korp,3000
Nikita Borisenko,2000
Sitarama Raju,1000'''


try: 
    with open("D:\\Oplata_truda.txt", "w", encoding="utf-8") as file:
        file.write(text)

except Exception as error:
    print(f"Файл не відкрився правильно, помилка --> {error}")

def total_salary(path):
    total_cash = 0
    average_salary = 0
    try:
        with open("D:\\Oplata_truda.txt", "r", encoding="utf-8") as file:
            for line in file:
                salary = line.split(",")
                total_cash = total_cash + int(salary[1])
                average_salary = average_salary + 1
            average = total_cash / average_salary
            return (total_cash, average)
    except Exception as error:
        print(f"Виникла помилка --> {error}")
    
total_cash, average = total_salary("D:\\Oplata_truda.txt")
print(f"Загальна сума заробітної плати: {total_cash}, Середня заробітна плата: {average}")
