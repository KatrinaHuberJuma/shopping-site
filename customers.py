"""Customers at Hackbright."""


class Customer(object):
    """Ubermelon customer."""

    def __init__(self, firstname, lastname, email, password):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password

    def __repr__(self):
        """Convenience method to show information about customer in console."""

        return "<Customer: %s %s, %s>" % (self.firstname, self.lastname, self.email)


def read_customers_from_file(filepath):
    """Read customer data and populate dictionary of customers

    Dictionary will be {email: Customer object}
    """

    customers = {}

    for line in open(filepath):
        (first_name,
         last_name,
         email,
         password) = line.strip().split("|")

        customers[email] = Customer(first_name,
                                    last_name,
                                    email,
                                    password)

    return customers 



def get_by_email(email):
    """Return the customer object at the given email"""

    return customers.get(email)


customers = read_customers_from_file("customers.txt")