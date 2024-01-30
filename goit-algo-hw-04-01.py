text = '''Alex Korp,3000
Nikita Borisenko,2000
Sitarama Raju,1000'''

with open("D:\\salary_file.txt", "w", encoding="utf-8") as file:
    file.write(text) 
def total_salary(path):
    total = 0
    count = 0

    with open("D:\\salary_file.txt", "r", encoding="utf-8") as file:
        for line in file:
            salary = line.split(",")[1]
            total += int(salary)
            count += 1
    average = total / count
    return (total, average)

total, average = total_salary("D:\\salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
