""" Take customer data and create Customer instances for each customer """
from customer import Customer

def organize_customer_data(customer_file_path):
    """Read customer file and return list of customer objects.

    Read file at customer_file_path and create a customer object containing
        customer information.

    """

    customers = []

    customer_file = open(customer_file_path)

    # Process a file like:
    #
    #   customer-name | email | street | city | zipcode
    #   Hu Mcconnell|et.lacinia@augueeutempor.edu|250-9855 Euismod Road|Labrecque|71616

    for line in customer_file:
        customer_data = line.strip().split("|")
        name, email, street, city, zipcode = customer_data

        new_customer = Customer(name, email, street, city, zipcode)
        customers.append(new_customer)

    return customers