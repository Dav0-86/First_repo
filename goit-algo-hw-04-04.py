# Напишіть консольного бота помічника, який розпізнаватиме команди, що вводяться з клавіатури, 
# та буде відповідати відповідно до введеної команди.


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return f"Contact {name} ---> phone number {phone} added."

def change_contact(args, contacts):
    if len(args) != 2:
        return "Invalid arguments. You need to provide a name and a phone number."
    name, phone = args
    if name not in contacts:
        return f"{name} not found. You need to provide an existing contact name."
    contacts[name] = phone
    return f"Contact {name} updated phone number to -> {phone}."

def show_phone(args, contacts):
    name = args[0]
    if name not in contacts:
        return f"{name} not found. You need to provide an existing contact name."
    else:
        return f" Subscriber's {name}, phone number ---> {contacts[name]}"
    
def show_all(*args):
    result = []
    for contacts in args:
        for name, phone in contacts.items():
            result.append(f"{name}: {phone}")
    return result




def main(welcome_message=True):
    contacts = {}
    if welcome_message:
        print("Welcome to the assistant bot!")
    while True:
        try:
            user_input = input("Enter a command: ")
            command, *args = parse_input(user_input)

            if command in ["close", "exit"]:
                print("Good bye!")
                break
            elif command == "hello":
                print("How can I help you?")
            elif command == "add":
                print(add_contact(args, contacts))
            elif command == "change":
                print(change_contact(args, contacts))
            elif command == "phone":
                print(show_phone(args, contacts))
            elif command == "show_all":
                print(show_all(contacts))
            else:
                print("Invalid command.")
        except Exception as e:
            print(f'''Error {e}. \n{"-"*52}\nYou entered incorrect information, please try again"''')
            return main(welcome_message=False)

        

if __name__ == "__main__":
    main()


