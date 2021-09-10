import src.Extract_team_4_project as extract
import src.Transform_team_4_project as transform
import src.db_script as database


def etl(filename):
    customers_list = []
    extract.extract_csv_info(filename, customers_list)
    
    print(len(customers_list), 'extracted data length')
    
    clean_data = []
    transform.transform_data(customers_list, clean_data)
    
    print(len(clean_data), 'transformed data length')
    # try:    
    #     database.create_database()
    # except:
    #     pass
    
    connection = database.create_connection()

    database.create_table_branch_table(connection)
    database.create_table_purchase_table(connection)
    database.create_table_products_table(connection)
    database.create_table_purchase_product_table(connection)
    
    for row in clean_data:
        database.insert_into_branch_table(connection, row["branch"])
        database.insert_into_purchase_table(connection, row["date"], row["time"], row["total"], database.get_location_id(row["branch"]), row["payment type"])
        
        for item in row["basket"]:
            database.insert_into_products_table(connection, item["name"], item["price"])
            database.insert_into_purchase_product_table(connection, row["date"], row["time"], database.get_product_id(item["name"]), item["quantity"])
    
    connection.close()
    print('etl function fin')
        

# etl('2021-02-23-isle-of-wight.csv')