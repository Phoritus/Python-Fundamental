import mysql.connector
from contextlib import contextmanager


@contextmanager
def connection(commit=False):
    connect = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '12345',
        database = 'expense_manager'
    )

    if connect.is_connected():
        print('Connection Successful')
    else:
        print('Connection Error')

    cursor = connect.cursor(dictionary=True)

    yield cursor

    if commit:
        connect.commit()
    cursor.close()
    connect.close()

def get_all_data():
    with connection() as cursor:
        cursor.execute("SELECT * FROM expenses;")
        expenses = cursor.fetchall()
        for data in expenses:
            print(data)


def get_by_date(date):
    with connection() as cursor:
        cursor.execute("SELECT * FROM expenses where expense_date= %s ;",(date,))
        expenses = cursor.fetchall()
        for data in expenses:
            print(data)


def insert_data(id,date,amount,category,notes):
    with connection(commit=True) as cursor:
        cursor.execute("insert into expenses (id,expense_date,amount,category,notes) values (%s,%s,%s,%s,%s);",
                       (id,date,amount,category,notes))


def delete_data(ids):
    with connection(commit=True) as cursor:
        cursor.execute("delete from expenses where id = %s ;",ids)

def get_by_id(ids):
    with connection() as cursor:
        cursor.execute("select * from expenses where id = %s ;",ids)
        expenses = cursor.fetchall()
        for data in expenses:
            print(data)

if __name__ == '__main__':
    get_by_id([2])