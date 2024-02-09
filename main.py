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
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Invalid phone number")
        super().__init__(value)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        new_phone = Phone(phone)
        if new_phone not in self.phones:
            self.phones.append(new_phone)
        else:
            raise ValueError("Phone number already exists")

    def remove_phone(self, phone):
        phone = Phone(phone)
        if phone in self.phones:
            self.phones.remove(phone)
        else:
            raise ValueError("Phone number not found")

    def find_phone(self, phone):
        phone_obj = Phone(phone)
        for phone_obj in self.phones:
            if phone_obj.value == phone_obj.value:
                return str(phone_obj)
    
        return None


    def edit_phone(self, old_phone, new_phone):
        old_phone_obj = Phone(old_phone)
        new_phone_obj = Phone(new_phone)
        
        found = False
        for phone_obj in self.phones:
            if phone_obj.value == old_phone_obj.value:
                phone_obj.value = new_phone_obj.value
                found = True
                break
        
        if not found:
            raise ValueError("Phone number not found")

    def __str__(self):
        phones_str = '; '.join(str(phone) for phone in self.phones)
        return f"Contact name: {self.name.value}, phones: {phones_str}"


class AddressBook(UserDict):
    def __init__(self):
        super().__init__()  # Ініціалізуємо батьківський клас

    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        name_field = Name(name)
        return self.data.get(name_field.value)  # Використовуємо метод get, щоб отримати запис або None, якщо запис не знайдено

    def delete(self, name):
        name_field = Name(name)
        if name_field.value in self.data:
            del self.data[name_field.value]
        else:
            return None  # Повертаємо None, якщо запис не знайдено

if __name__ == "__main__":
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
    print(f"{found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
    book.delete("Jane")
