import psycopg2
import boto3

def create_connection():
    client = boto3.client('redshift', region_name='eu-west-1')
    
    REDSHIFT_USER = "awsuser"
    REDSHIFT_CLUSTER = "redshiftcluster-fbtitpjkbelw"
    REDSHIFT_HOST = "redshiftcluster-fbtitpjkbelw.cnvqpqjunvdy.eu-west-1.redshift.amazonaws.com"
    REDSHIFT_DATABASE = "team4db"
    
    
    creds = client.get_cluster_credentials(
      DbUser=REDSHIFT_USER,
      DbName=REDSHIFT_DATABASE,
      ClusterIdentifier=REDSHIFT_CLUSTER,
      DurationSeconds=3600)
    
    conn = psycopg2.connect(
      user=creds['DbUser'], 
      password=creds['DbPassword'],
      host=REDSHIFT_HOST,
      database=REDSHIFT_DATABASE,   
      port=5439
    )
    
    return conn

# def create_database():
    
#     con = psycopg2.connect(
#     host="localhost",
#     user="root",
#     password="password" )

#     cur = con.cursor()
#     con.autocommit = True
#     cur.execute('create database infinity_cafes')
#     cur.close()
#     con.close()

def create_table_purchase_table(con):
    
    cur = con.cursor()
    cur.execute('''create table if not exists purchase_table 
                (purchase_id INT IDENTITY(1,1), purchase_date DATE NOT NULL,
                purchase_time TIME UNIQUE NOT NULL,
                purchase_total FLOAT NOT NULL,
                branch_id INTEGER NOT NULL,
                payment_type VARCHAR(50) NOT NULL,
                PRIMARY KEY (purchase_date, purchase_time, branch_id),
                FOREIGN KEY(branch_id) REFERENCES branch_table(branch_id))''')
    con.commit()
    cur.close()
    

def create_table_branch_table(con):
    
    cur = con.cursor()
    cur.execute('''create table if not exists branch_table 
                (branch_id  INT IDENTITY(1,1),
                branch_location TEXT UNIQUE NOT NULL,
                PRIMARY KEY(branch_id))''')
    con.commit()
    cur.close()
    
    
def create_table_products_table(con):
    
    cur = con.cursor()
    cur.execute('''create table if not exists products_table 
                (product_id  INT IDENTITY(1,1), 
                product_name VARCHAR (100) UNIQUE NOT NULL, 
                product_price FLOAT NOT NULL, 
                PRIMARY KEY(product_id))''')
    con.commit()
    cur.close()
    

def create_table_purchase_product_table(con):
    
    cur = con.cursor()
    cur.execute('''create table if not exists purchase_product_table 
                (purchase_date DATE NOT NULL, 
                purchase_time TIME NOT NULL, 
                product_id INTEGER NOT NULL, 
                amount INTEGER, 
                PRIMARY KEY (purchase_date, purchase_time, product_id), 
                FOREIGN KEY (product_id) REFERENCES products_table(product_id))''')
    con.commit()
    cur.close()
    

def insert_into_branch_table(con, value):
    
    command = '''INSERT INTO branch_table
                (branch_location) 
                VALUES (%s) on conflict (branch_location) do nothing'''
    
    val = (value,)
    cur = con.cursor()
    cur.execute(command, val)
    con.commit()
    cur.close()
    
    
def insert_into_products_table(con, name, price):
    
    command = '''INSERT INTO products_table 
                (product_name, product_price) 
                VALUES (%s, %s) on conflict (product_name) do nothing'''
    
    val = (name, price,)
    cur = con.cursor()
    cur.execute(command, val)
    con.commit()
    cur.close()
    

def insert_into_purchase_table(con, date, time, total, branch, payment):
    
    command = '''INSERT INTO purchase_table 
                (purchase_date, purchase_time, purchase_total, branch_id, payment_type) 
                VALUES (%s, %s, %s, %s, %s) on conflict (purchase_date, purchase_time, branch_id) do nothing'''
    
    val = (date, time, total, branch, payment,)
    cur = con.cursor()
    cur.execute(command, val)
    con.commit()
    cur.close()
    
    
def insert_into_purchase_product_table(con, date, time, product_id, amount):
    
    command = '''INSERT INTO purchase_product_table 
                (purchase_date, purchase_time, product_id, amount) 
                VALUES (%s, %s, %s, %s) on conflict (purchase_date, purchase_time, product_id) do nothing'''
    
    val = (date, time, product_id, amount,)
    cur = con.cursor()
    cur.execute(command, val)
    con.commit()
    cur.close()
    

def get_location_id(con, branch):
    
    command = f'SELECT branch_id FROM branch_table WHERE branch_location = %s'
    cur = con.cursor()
    val = (branch,)
    cur.execute(command,val)
    record = cur.fetchall()
    cur.close()
    return record[0][0]

def get_product_id(con, product):
    
    command = f'SELECT product_id FROM products_table WHERE product_name = %s'
    cur = con.cursor()
    val = (product,)
    cur.execute(command,val)
    record = cur.fetchall()
    cur.close()
    return record[0][0]
