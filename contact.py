class Contact:

    Contact_list = []

    def __init__(self, first_name, second_name, phone, email) -> None:
        self.first_name = first_name
        self.second_name = second_name
        self.email = email
        self.phone = phone

    def save_contact(self):
        Contact.Contact_list.append(self)
        print(Contact.Contact_list)


    def delete_contact(self):
        Contact.Contact_list.remove(self)

    @classmethod
    def filter_contact_by_number(cls, number):
        filtered = [contact for contact in cls.Contact_list if contact.phone == number]
        return filtered


    @classmethod
    def display_all_contacts(cls):
        return cls.Contact_list

    def __str__(self) -> str:
        return f'Dictionary with first name as {self.first_name} and second name as {self.second_name} '