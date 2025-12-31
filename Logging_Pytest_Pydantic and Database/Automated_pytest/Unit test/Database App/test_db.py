import pytest
from customer_db import CustomersDB

@pytest.fixture
def db():
    db = CustomersDB()
    db.connect()
    yield db
    db.clear_customer()
    db.close()

def test_insert_db(db):

    db.insert_customer('Kemera','Kemera@gmail.com')
    customer = db.get_customer_name('Kemera')

    assert customer is not None
    assert customer['name'] == 'Kemera'
    assert customer['email'] == 'Kemera@gmail.com'


def test_get_alldb(db):

    db.insert_customer('Kemera', 'Kemera@gmail.com')
    db.insert_customer('Janinja', 'Janinja@gmail.com')
    customer = db.get_all_customers()

    assert len(customer) == 2