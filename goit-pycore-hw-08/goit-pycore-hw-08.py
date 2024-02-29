from collections import deque
from collections import UserDict
from datetime import datetime, timedelta
import pickle

#Error
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Give me existing name in AddressBook"
        except IndexError:
            return "Give me name, and I'll show the number for this user"
        except TypeError:
            return "Give me name, and date Birthday for user"
    return inner

# Classes 
class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, name):
        self.name = name


class Phone(Field):
    def __init__(self, number):
        self.number = number

    def validate_phone(self):
        try:
            if len(self.number) == 10:
                return True
        except:
            raise ValueError("Phone number must be 10 digits long")


class Birthday(Field):
    def __init__(self, value):
        self.value = value
        try:
            datetime.strptime(value, "%d-%m-%Y")
        except ValueError:
            raise ValueError("The date must be in the format dd-mm-yyyy")


class Record:
    def __init__(self, name, phone):
        self.phone = [Phone(phone)]
        self.name = Name(name)
        self.birthday = None

    @input_error
    def add_phone(self, phone):
        new_phone = Phone(phone)
        if new_phone.validate_phone():
            self.phone.append(new_phone)

    @input_error
    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    @input_error
    def remove_phone(self, phone):
        self.phone = [p for p in self.phone if p.number != phone]

    @input_error
    def edit_phone(self, old_phone, new_phone):
        for p in self.phone:
            if p.number == old_phone:
                new_phone_obj = Phone(new_phone)
                if new_phone_obj.validate_phone():
                    p.number = new_phone

    def __str__(self):
        return f"Contact phones: {'; '.join(p.number for p in self.phone)}"


class AddressBook(UserDict):
    def add_record(self, name, phone):
        self.data[name] = Record(name, phone)

    @input_error
    def add_birthday(self, name, birthday):
        if name in self.data:
            record = self.data[name]
            if isinstance(record, Record):
                record.add_birthday(birthday)
                return f"Birthday added for contact {name}."
            else:
                return f"Contact {name} is not a Record instance."
        else: 
            return f"There is no such contact: {name}."

    @input_error
    def show_birthday(self, name):
        if name in self.data and self.data[name].birthday is not None:
            return f"{name}'s birthday is on {self.data[name].birthday.value}."
        else:
            return f"No birthday information for contact {name}."


    def birthdays(self):
        today_day=datetime.today().date()
        upcoming_birthdays = []
        for name, record in self.data.items():
            if record.birthday is not None:
                birthday_date = datetime.strptime(record.birthday.value, "%d-%m-%Y")
                birthday_date = birthday_date.replace(year=today_day.year)
                if birthday_date.date() >= datetime.now().date() and birthday_date.date() <= (datetime.now() + timedelta(days=7)).date():
                    upcoming_birthdays.append(f"{name}'s birthday is on {record.birthday.value}.")
        return upcoming_birthdays if upcoming_birthdays else "No birthdays in the next week."



# OPERATION MODE
@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, AddressBook):
    name, phone = args
    new_phone = Phone(phone)
    if new_phone.validate_phone():
        if name not in AddressBook.data:
            AddressBook.add_record(name, phone)
            return "Contact added."
        else: 
            return f"Contact {name} is already in your contact list"
    else:
        return "Phone number must be 10 digits long"
    
@input_error
def change_contact(args, AddressBook):
    name, phone = args
    if name in AddressBook:
        AddressBook[name] = phone
        return f"Contact {name} updated phone number to -> {phone}."
    else: 
        return f"No such contact: {name}."

@input_error
def show_phone(args, AddressBook):
    name = args[0]
    return f"Subscriber's {name}, phone number ---> {AddressBook[name]}"


def show_all(*args):
    result = []
    result.append(f"{'Contact name':<15}|{'Phone number':<15}|{'Birthday':<15}")
    result.append(f"{'-'*15}|{'-'*15}|{'-'*15}")
    for AddressBook in args:
        for name, record in AddressBook.data.items():
            phones = '; '.join(p.number for p in record.phone)
            birthday = record.birthday.value if record.birthday else "Birthday not specified"
            result.append(f"{name:<15}|{phones:<15}|{birthday:<15}")
    return result



# main
try:
    with open('addressbook.pkl', 'rb') as input:
        book = pickle.load(input)
except FileNotFoundError:
    book = AddressBook()

def main():
    book = AddressBook()
    user_inputs = deque(maxlen=100)
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        user_inputs.append(user_input)
        command, *args = parse_input(user_input)
        user_input_all = {
            'add': lambda args: add_contact(args, book),
            "change": lambda args: change_contact(args, book),
            "phone": lambda args: show_phone(args, book),
            'телефон': lambda args: show_phone(args, book),
            'изменить': lambda args: change_contact(args, book),
            "добавить": lambda args: add_contact(args, book),
            "add-birthday": lambda args: book.add_birthday(*args),
            "день_рождение": lambda args: book.add_birthday(*args),
            "show-birthday": lambda args: book.show_birthday(*args)
        }

        if command in ["close", "exit"]:
            print("Good bye!")
            print(f"Log of all your entered data >>> {user_inputs}")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command in user_input_all:
            func = user_input_all.get(command)
            print(func(args))
        elif command in ["show_all", "all", "все номера", "все"]:
            print('-'*45)
            print('\n'.join(show_all(book)))
            print('-'*45)
        elif command in ["birthdays", "дни_рождения", "bd", "др"]:
            print('-'*45)
            print('\n'.join(book.birthdays()))
            print('-'*45)
        else:
            print("Invalid command.")



if __name__ == "__main__":
    with open('addressbook.pkl', 'wb') as output:
        pickle.dump(book, output, pickle.HIGHEST_PROTOCOL)
