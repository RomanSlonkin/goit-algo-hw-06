from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        if not value:
            raise ValueError("Name could not be empty.")
        super().__init__(value)

class Phone(Field):
    def __init__(self, value):
        if not(value.isdigit() and len(value) == 10):
            raise ValueError("Phone number must be 10 numbers")
        super().__init__(value)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
    
    def add_phone(self, phone):
        phone = Phone(phone)
        self.phones.append(phone)

    def remove_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
        return("There is no such phone in the contact list.")

    def edit_phone(self, old_phone, new_phone):
        old_phone = Phone(old_phone)
        new_phone = Phone(new_phone)
        for idx, phone in enumerate(self.phones):
            if phone.value == old_phone.value:
                self.phones[idx] = new_phone
                return
        return "There is no such phone in the contact list."
        

    def find_phone(self, phone):
        phone = Phone(phone)
        for p in self.phones:
            if p.value == phone.value:
                return phone
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def delete(self, name):
        if name in self.data:
            del self.data[name]
        else:
             return "There is no contact with this name."

    def find(self, name):
        return self.data.get(name, None)

    def __str__(self):
        contacts = [str(record) for record in self.data.values()]
        return "\n".join(contacts)

address_book = AddressBook()
record = Record("Іван")
record.add_phone("1234567890")
address_book.add_record(record)

# Знайти запис
print(address_book.find("Іван"))

# Видалити запис
address_book.delete("Іван")

# Додати і вивести всі записи
print(address_book)


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
     
print(book)
# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")
john.remove_phone("1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: John: 5555555555

# Видалення запису Jane
book.delete("Jane")
