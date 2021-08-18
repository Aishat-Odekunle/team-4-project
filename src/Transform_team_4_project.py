import Extract_team_4_project as extract
import pprint

clean_data = []

def is_number(string):
    try:
        float(string)
        return True
    except ValueError:
        return False
    
def transform_data(list_to_read_from, list_to_append_to):
    for row in list_to_read_from:
        row.pop(2)
        row.pop(-1)
        order = row[2].split(',')
        
        products = []
        prices = []
        
        for i in order:
            if i == '':
                order.remove(i)
        row[2] = ','.join(order)
        
        for i in row[2].split(','):
            if is_number(i):
                prices.append(i)
        
        order_list = row[2].split(',')
        for i in range(len(order_list)):
            if is_number(order_list[i]):
                order_list[i] = ':'
        order_list = ' '.join(order_list)
        order_list = order_list.split(':')
        
        for i in range(len(order_list)):
            if order_list[i] != '':
                products.append(order_list[i])
                
        transformed = {}
        transformed["timestamp"] = row[0]
        transformed["branch"] = row[1]
        transformed["basket"] = [{"name": f.strip(), "price": format(float(b), '.2f')} for f, b in zip(products, prices)]
        transformed["payment type"] = row[3]
        transformed["total"] = format(float(row[4]), '.2f')
            
        list_to_append_to.append(transformed)
    
    
transform_data(extract.customers_list, clean_data)


pprint.pprint(clean_data[8])


