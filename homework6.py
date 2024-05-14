from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        if len(value) != 10 or not value.isdigit():
            raise ValueError("Phone number must be 10 digits.")
        super().__init__(value)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        try:
            self.phones.append(Phone(phone))
        except ValueError as e:
            print(e)

    def edit_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                try:
                    phone.value = new_phone
                except ValueError as e:
                    print(e)
                return
        print("Phone not found.")
    
    def remove_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
                print(f"Phone {phone} removed successfully.")
                return
        print("Phone not found.")

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        print("Phone not found.")
        return None

    def __str__(self):
        return f"Contact name: {self.name}, phones: {'; '.join(str(p) for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def delete(self, name):
        if name in self.data:
            del self.data[name]
        else:
            print("Record not found.")

    def find(self, name):
        if name in self.data:
            return self.data[name]
        else:
            print("Record not found.")

# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: John: 5555555555

# Видалення запису Jane
book.delete("Jane")
