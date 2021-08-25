import psycopg2

def create_database():
    
    con = psycopg2.connect(
    host="localhost",
    user="root",
    password="password" )

    cur = con.cursor()
    con.autocommit = True
    cur.execute('create database infinity_cafes')
    cur.close()
    con.close()

def create_table_purchase_table():
    con = psycopg2.connect(
    host="localhost",
    user="root",
    database= "infinity_cafes",
    password="password" )
    
    cur = con.cursor()
    cur.execute('create table if not exists purchase_table (purchase_id SERIAL, purchase_date DATE NOT NULL, purchase_time TIME NOT NULL, purchase_total MONEY NOT NULL, branch_id INTEGER, payment_type VARCHAR(50) NOT NULL,PRIMARY KEY (purchase_id), FOREIGN KEY(branch_id) REFERENCES branch_table(branch_id))')
    con.commit()
    cur.close()
    con.close()

def create_table_branch_table():
    con = psycopg2.connect(
    host="localhost",
    user="root",
    database= "infinity_cafes",
    password="password")
    
    cur = con.cursor()
    cur.execute('create table if not exists branch_table (branch_id SERIAL, branch_location TEXT NOT NULL, PRIMARY KEY(branch_id))')
    con.commit()
    cur.close()
    con.close()
    
def create_table_products_table():
    con = psycopg2.connect(
    host="localhost",
    user="root",
    database= "infinity_cafes",
    password="password")
    
    cur = con.cursor()
    cur.execute('create table if not exists products_table (product_id SERIAL, product_name VARCHAR (100) NOT NULL, product_price MONEY NOT NULL, PRIMARY KEY(product_name))')
    con.commit()
    cur.close()
    con.close()

def create_table_purchase_product_table():
    con = psycopg2.connect(
    host="localhost",
    user="root",
    database= "infinity_cafes",
    password="password")
    
    cur = con.cursor()
    cur.execute('create table if not exists purchase_product_table (purchase_date DATE NOT NULL , product_id INTEGER NOT NULL, amount INTEGER, FOREIGN KEY(purchase_date) REFERENCES purchase_table(purchase_date), FOREIGN KEY (product_id) REFERENCES products_table(product_id))')
    con.commit()
    cur.close()
    con.close()
    
   
try:    
    create_database()
except:
    pass

create_table_branch_table()
create_table_purchase_table()
create_table_products_table()
create_table_purchase_product_table()


def insert_into_branch_table(value):
    con = psycopg2.connect(
    host="localhost",
    user="root",
    database= "infinity_cafes",
    password="password")
    
    command = "INSERT INTO branch_table (branch_location) VALUES (%s)"
    
    val = (value,)
    cur = con.cursor()
    cur.execute(command, val)
    con.commit()
    cur.close()
    con.close()
    
def insert_into_products_table(name, price):
    con = psycopg2.connect(
    host="localhost",
    user="root",
    database= "infinity_cafes",
    password="password")
    
    command = "INSERT INTO products_table (product_name, product_price) VALUES (%s, %s) on conflict (product_name) do nothing"
    
    val = (name, price,)
    cur = con.cursor()
    cur.execute(command, val)
    con.commit()
    cur.close()
    con.close()

def insert_into_purchase_table(date, time, total, branch, payment):
    con = psycopg2.connect(
    host="localhost",
    user="root",
    database= "infinity_cafes",
    password="password")
    
    command = "INSERT INTO purchase_table (purchase_date, purchase_time, purchase_total, branch_id, payment_type) VALUES (%s, %s, %s, %s, %s)"
    
    val = (date, time, total, branch, payment,)
    cur = con.cursor()
    cur.execute(command, val)
    con.commit()
    cur.close()
    con.close()

def get_location_id(branch):
    con = psycopg2.connect(
    host="localhost",
    user="root",
    database= "infinity_cafes",
    password="password")
    
    command = f'SELECT branch_id FROM branch_table WHERE branch_location = %s'
    cur = con.cursor()
    val = (branch,)
    cur.execute(command,val)
    record = cur.fetchall()
    cur.close()
    con.close()
    return record[0][0]

def get_product_id(product):
    con = psycopg2.connect(
    host="localhost",
    user="root",
    database= "infinity_cafes",
    password="password")
    
    command = f'SELECT product_id FROM products_table WHERE product_name = %s'
    cur = con.cursor()
    val = (product,)
    cur.execute(command,val)
    record = cur.fetchall()
    cur.close()
    con.close()
    return record[0][0]

# insert_into_products_table('Large Chai Latte', 2.40)
insert_into_purchase_table('2021-02-23', '09:00:48', 8.40, get_location_id('Isle of Wight'), 'CASH')


# print(get_product_id('Large Chai Latte'))
