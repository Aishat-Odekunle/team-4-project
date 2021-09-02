import Extract_team_4_project as extract
import Transform_team_4_project as transform
import db_script as database

def etl(filename):
    customers_list = []
    extract.extract_csv_info(filename, customers_list)
    
    clean_data = []
    transform.transform_data(customers_list, clean_data)
    
    try:    
        database.create_database()
    except:
        pass

    database.create_table_branch_table()
    database.create_table_purchase_table()
    database.create_table_products_table()
    database.create_table_purchase_product_table()
    
    for row in clean_data:
        database.insert_into_branch_table(row["branch"])
        database.insert_into_purchase_table(row["date"], row["time"], row["total"], database.get_location_id(row["branch"]), row["payment type"])
        
        for item in row["basket"]:
            database.insert_into_products_table(item["name"], item["price"])
            database.insert_into_purchase_product_table(row["date"], row["time"], database.get_product_id(item["name"]), item["quantity"])
        
    print('db function fin')
        

etl('2021-02-23-isle-of-wight.csv')