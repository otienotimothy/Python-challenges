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


    def __str__(self) -> str:
        return f'Dictionary with first name as {self.first_name} and second name as {self.second_name} '