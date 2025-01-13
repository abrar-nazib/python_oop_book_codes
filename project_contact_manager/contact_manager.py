from typing import List


# Example of extending base classes
class ContactList(list):
    def search(self, name: str):
        """Return all contacts that contain the search value in their name"""
        matching_contacts = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts


class MailSender:
    def send_mail(self, message: str):
        print(f"Sending mail {message} to {self.email}")  # Do I have self.email?


# Class
class Contact:
    all_contacts = ContactList()

    def __init__(self, name: str, email: str, **kwargs):
        super().__init__(**kwargs)
        self.name: str = name
        self.email: str = email
        Contact.all_contacts.append(self)

    def __repr__(self) -> str:
        return f"{self.name} - {self.email}"


class EmailableContact(Contact, MailSender):
    pass


# Example of inheritence
class Supplier(Contact):
    def order(self, order):
        print(f"If this were a real system we would send {order} order to {self.name}")


class AddressHolder:
    def __init__(self, street: str, city: str, state: str, code: str, **kwargs):
        super().__init__(**kwargs)
        self.street = street
        self.city = city
        self.state = state
        self.code = code


class Friend(Contact):
    def __init__(self, name: str, email: str, phone: str):
        super().__init__(name, email)
        self.phone = phone

    def __repr__(self):
        return f"{super().__repr__()} - {self.phone}"


if __name__ == "__main__":
    c = Contact("Nazib Abrar", "abrarnazib@gmail.com")
    s = Supplier("Abrar Nazib", "nazibabrar@gmail.com")
    f = Friend("Hasibur Rahman Naheen", "naheen@gmail.com", "0192252318")
    e = EmailableContact("Humam Hossain", "humam@gmail.com")
    print(c.all_contacts)
    e.send_mail("Hello!")
    print(c.all_contacts)
    # s.order("Book")
    # print(Contact.all_contacts.search("Abrar"))
