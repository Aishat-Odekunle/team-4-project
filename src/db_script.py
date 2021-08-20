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
    cur.execute('create table if not exists purchase_table (purchase_id SERIAL, purchase_date DATE NOT NULL, purchase_time TIME NOT NULL, purchase_total MONEY NOT NULL, branch_id SERIAL, payment_type VARCHAR(50) NOT NULL,PRIMARY KEY (purchase_id), FOREIGN KEY(branch_id) REFERENCES branch_table(branch_id))')
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
    cur.execute('create table if not exists branch_table (branch_id SERIAL, branch_location VARCHAR(100) NOT NULL, PRIMARY KEY(branch_id))')
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
    cur.execute('create table if not exists products_table (product_id SERIAL, product_name VARCHAR (100) NOT NULL, product_price MONEY NOT NULL, PRIMARY KEY(product_id))')
    con.commit()
    cur.close()
    con.close()

def create_table_basket_table():
    con = psycopg2.connect(
    host="localhost",
    user="root",
    database= "infinity_cafes",
    password="password")
    
    cur = con.cursor()
    cur.execute('create table if not exists basket_table (basket_id SERIAL NOT NULL, purchase_id SERIAL NOT NULL, product_id SERIAL NOT NULL, amount INTEGER, FOREIGN KEY(purchase_id) REFERENCES purchase_table(purchase_id), FOREIGN KEY (product_id) REFERENCES products_table(product_id) )')
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
create_table_basket_table()