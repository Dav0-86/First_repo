def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."

    return inner

def show_phone_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return f"Name not found. You need to provide an existing contact name."
        except IndexError:
            return f"You must enter a name to search for a phone number"

    return inner


def parse_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "You have not entered anything. Please repeat your request"

    return inner





@parse_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return f"Contact {name} updated phone number to -> {phone}."

@show_phone_error
def show_phone(args, contacts):
    name = args[0]
    return f"Subscriber's {name}, phone number ---> {contacts[name]}"
    
def show_all(*args):
    result = []
    for contacts in args:
        for name, phone in contacts.items():
            result.append(f"{name}: {phone}")
    return result




def main():
    contacts = {}
    user_inputs = []
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        user_inputs.append(user_input)
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            print(f"Log of all your entered data >>> {user_inputs}")
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
        elif command == "all":
            print(show_all(contacts))    
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
