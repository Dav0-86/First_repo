# # Определяем функцию parse_input, которая принимает ввод пользователя
# def parse_input(user_input):
#     # Разделяем ввод пользователя по пробелам и получаем команду и аргументы
#     cmd, *args = user_input.split()
#     # Удаляем пробелы в начале и конце команды и приводим ее к нижнему регистру
#     cmd = cmd.strip().lower()
#     # Возвращаем команду и аргументы
#     return cmd, *args

# # Определяем функцию add_contact, которая принимает аргументы и словарь контактов
# def add_contact(args, contacts):
#     # Получаем имя и телефон из аргументов
#     name, phone = args
#     # Добавляем имя и телефон в словарь контактов
#     contacts[name] = phone
#     # Возвращаем сообщение об успешном добавлении
#     return "Контакт добавлен."


# def change_contact(username, phone, contacts):
#     # Перевіряємо, чи існує контакт з таким ім'ям в словнику
#     if username in contacts:
#         # Змінюємо номер телефону для контакту
#         contacts[username] = phone
#         # Повертаємо рядок "Contact changed." в якості відповіді
#         return "Contact changed."
#     else:
#         # Якщо контакту з таким ім'ям немає в словнику, повертаємо рядок "Contact not found." в якості відповіді
#         return "Contact not found."


# def get_all(contacts):
#     # Ініціалізуємо порожній рядок для зберігання результату
#     result = ""
#     # Для кожної пари ключ-значення в словнику
#     for username, phone in contacts.items():
#         # Додаємо рядок з ім'ям і номером телефону до результату, розділяючи їх пробілом
#         result += f"{username} {phone}\n"
#     # Повертаємо рядок з усіма контактами в якості відповіді
#     return result





# def get_phone(username, contacts):
#     # Перевіряємо, чи існує контакт з таким ім'ям в словнику
#     if username in contacts:
#         # Повертаємо рядок з номером телефону в якості відповіді
#         return contacts[username]
#     else:
#         # Якщо контакту з таким ім'ям немає в словнику, повертаємо рядок "Contact not found." в якості відповіді
#         return "Contact not found."


# # Определяем основную функцию main, которая запускает бота
# def main():
#     # Создаем пустой словарь для хранения контактов
#     contacts = {}
#     # Выводим приветственное сообщение
#     print("Добро пожаловать в бот-помощник!")
#     # Запускаем бесконечный цикл
#     while True:
#         # Получаем ввод пользователя
#         user_input = input("Введите команду: ")
#         # Парсим ввод пользователя и получаем команду и аргументы
#         command, *args = parse_input(user_input)

#         # Если команда равна "close" или "exit"
#         if command in ["close", "exit"]:
#             # Выводим прощальное сообщение
#             print("До свидания!")
#             # Прерываем цикл
#             break
#         # Если команда равна "hello"
#         elif command == "hello":
#             # Выводим вопрос о том, как мы можем помочь
#             print("Как я могу вам помочь?")
#         # Если команда равна "add"
#         elif command == "add":
#             # Вызываем функцию add_contact с аргументами и словарем контактов и выводим результат
#             print(add_contact(args, contacts))
#         # В противном случае
#         else:
#             # Выводим сообщение об неверной команде
#             print("Неверная команда.")


# # Если этот файл запускается как основная программа
# if __name__ == "__main__":
#     # Вызываем функцию main
#     main()
