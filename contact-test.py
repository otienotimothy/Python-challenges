import unittest
from contact import Contact


class ContatTest(unittest.TestCase):
    '''
        Tests for the contact creation class
    '''

    def setUp(self):
        self.new_contact = Contact(
            'James', 'Rodriguez', '0711135616', 'james@rodriguez@example.com')

    def tearDown(self):
        Contact.Contact_list = []

    def test_init(self):
        self.assertEqual(self.new_contact.first_name, 'James')
        self.assertEqual(self.new_contact.second_name, 'Rodriguez')
        self.assertEqual(self.new_contact.email, 'james@rodriguez@example.com')
        self.assertEqual(self.new_contact.phone, '0711135616')

    def test_save_contact(self):
        self.new_contact.save_contact()
        self.assertEqual(len(Contact.Contact_list), 1)

    def test_save_multiple_contacts(self):
        self.new_contact.save_contact()
        another_contact = Contact(
            'Paul', 'Pogba', '0711135616', 'pp@example.com')
        another_contact.save_contact()
        self.assertEqual(len(Contact.Contact_list), 2)

    def test_delete_contact(self):
        self.new_contact.save_contact()
        another_contact = Contact(
            'Paul', 'Pogba', '0711135616', 'pp@example.com')
        another_contact.save_contact()
        self.new_contact.delete_contact()
        self.assertEqual(len(Contact.Contact_list), 1)

    def test_filter_contacts(self):
        self.new_contact.save_contact()
        self.assertEqual(self.new_contact.filter_contact_by_number(
            '0711135616'), [self.new_contact])


    def test_display_contacts(self):
        self.new_contact.save_contact()
        self.assertEqual(Contact.display_all_contacts(), Contact.Contact_list)


if __name__ == '__main__':
    unittest.main()
