class CustomersDB:
    def __init__(self):
        self.customers = []
        self.ids = 1
        self.connection = None

    def connect(self):
        self.connection = 'Connection'
        print('Connected to the database.')

    def insert_customer(self, name, email):
        self.customers.append({
            'id': self.ids,
            'name': name,
            'email': email
        })
        self.ids += 1

    def get_all_customers(self):
        return self.customers

    def get_customer_name(self, name):
        for customer in self.customers:
            if customer['name'] == name:
                return customer
        return None

    def clear_customer(self):
        self.customers = []
        self.ids = 1

    def close(self):
        self.connection = None
        print('Database connection closed')
