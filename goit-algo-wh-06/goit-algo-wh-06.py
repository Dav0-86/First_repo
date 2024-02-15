from collections import UserDict

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
        return len(self.number) == 10

class Record:
    def __init__(self, phone):
        self.phone = [phone] 

    def add_phone(self, phone):
        self.phone.append(phone)

    def remove_phone(self, phone):
        if phone in self.phone:
            self.phone.remove(phone)

    def edit_phone(self, old_phone, new_phone):
        if old_phone in self.phone:
            index = self.phone.index(old_phone)
            self.phone[index] = new_phone

    def __str__(self):
        return f"Contact phones: {'; '.join(p.number for p in self.phone)}"

class AddressBook(UserDict):
    def add_record(self, name, phone):
        self.data[name] = phone


if __name__ == "__main__":

    book = AddressBook()
    name = Name("John")
    phone1 = Phone("1234567890")
    phone2 = Phone("5555555555")

    record = Record(phone1)
    record.add_phone(phone2)
    book.add_record("John", record)

    for name, record in book.data.items():
        print(record, book, name)
