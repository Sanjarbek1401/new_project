import psycopg2
from colorama import Fore
host = 'localhost'
user = 'postgres'
password = '1425'
database = 'n42'
port = 5432

conn = psycopg2.connect(host=host,
                        database=database,
                        user=user,
                        password=password,
                        port=port
                        )

cur = conn.cursor()

def print_response(message: str):
    print(Fore.BLUE + message + Fore.RESET)


create_table = '''
    create table if not exists test.product(
        id serial primary key,
        name varchar(30) not null,
        price int not null);

'''
cur.execute(create_table)
conn.commit()

def insert_testproduct():
    name = str(input("Enter product name:"))
    price = int(input("Enter product's price:"))
    insert_into_query = "Insert into test.Product(name,price) values (%s,%s);"
    insert_into_params = (name,price)
    cur.execute(insert_into_query,insert_into_params)
    conn.commit()
    print_response('Insert 0 1')
    
#insert_testproduct()
def select_all_product():
    select_query = 'select * from test.product;'
    cur.execute(select_query)
    rows = cur.fetchall()
    for row in rows:
        print_response(str(row))
#select_all_product()

def select_one_product():
    _id = int(input("Enter your product id:"))
    select_query = 'select * from test.product where id = %s;'
    cur.execute(select_query,(_id,))
    product = cur.fetchone()
    if product:
        print_response(str(product))
    else:
        print_response('No such product')
#select_one_product()

def update_product():
    select_all_product()
    _id = int(input("Enter your book id:"))
    name = str(input("Enter your new product:"))
    price = int(input("Enter your product's price:"))
    update_query = 'update test.product set name = %s, price = %s where id = %s;'
    update_query_params = (name,price,_id)
    cur.execute(update_query,update_query_params)
    conn.commit()
    print_response('Succesfully updated product')
#update_product() 

def delete_product():
    select_all_product()
    _id = int(input('Enter product id:'))
    delete_query = 'delete from test.product where id = %s;'
    cur.execute(delete_query,(_id,))
    conn.commit()
    print_response('Succesfully deleted product')
#delete_product()

def menu():
    try:
        print('Insert product  =>1')
        print('Select all product =>2')
        print('Delete product =>3')
        print('Select one product =>4')
        print('Update book =>5')
        choice = int(input('Enter your choice:'))
    except ValueError as e:
        choice = -1

    return choice
def run ():
    while True:
        choice = menu()
        match choice:
            case 1:
                insert_testproduct()
            case 2:
                select_all_product()
            case 3:
                delete_product()
            case 4:
                select_one_product()
            case 5:
                update_product()
            case _:
                break
if __name__=='__main__':
    run()
                        


    
