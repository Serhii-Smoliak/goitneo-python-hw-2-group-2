"""'This file contains classes and methods for managing an address book."""

from collections import UserDict


class Field:
    """'Base class for record fields."""

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    """'Class for storing contact name. Mandatory field."""

    def __init__(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        super().__init__(value)


class Phone(Field):
    """'Class for storing phone number. Has format validation (10 digits)."""

    def __init__(self, value):
        if not isinstance(value, str):
            raise ValueError("Phone number must be a string")
        if not value.isdigit():
            raise ValueError("Phone number must contain only digits")
        if len(value) != 10:
            raise ValueError("Phone number must contain exactly 10 digits")
        super().__init__(value)


class Record:
    """'Class for storing contact information,
    including name and list of phones."""

    def __init__(self, record_name):
        self.name = Name(record_name)
        self.phones = []

    def add_phone(self, phone_number):
        """'Method adds phone number, handles errors."""

        try:
            phone = Phone(phone_number)
            self.phones.append(phone)
        except ValueError as e:
            print(e)

    def remove_phone(self, phone_number):
        """'Method removes phone from list, handles absence."""

        for phone in self.phones:
            if phone.value == phone_number:
                self.phones.remove(phone)
                return
        print(f"Phone number {phone_number} not found")

    def edit_phone(self, old_phone_number, new_phone_number):
        """'Method edits phone number, handles errors & absence."""

        for phone in self.phones:
            if phone.value == old_phone_number:
                try:
                    new_phone = Phone(new_phone_number)
                    phone.value = new_phone.value
                    return
                except ValueError as e:
                    print(e)
        print(f"Phone number {old_phone_number} not found")

    def find_phone(self, phone_number):
        """'Method finds phone number, handles absence."""

        for phone in self.phones:
            if phone.value == phone_number:
                return phone.value
        print(f"Phone number {phone_number} not found")

    def __str__(self):
        return (
            f"Contact name: {self.name.value}, "
            f"phones: {'; '.join(str(p) for p in self.phones)}"
        )


class AddressBook(UserDict):
    """'Class for storing and managing records."""

    def add_record(self, new_record):
        """'Method adds record, handles existing."""

        self.data[new_record.name.value] = new_record

    def find(self, target_name):
        """'Method finds record by name, prints if absent."""

        if target_name in self.data:
            return self.data[target_name]
        else:
            print(f"Record for {target_name} not found")

    def delete(self, target_name):
        """'Method deletes record by name, prints if absent."""

        if target_name in self.data:
            del self.data[target_name]
        else:
            print(f"Record for {target_name} not found")
