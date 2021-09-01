import Extract_team_4_project as extract
import pprint
import datetime

clean_data = []

def format_date(var):
    ls = ['/', '.']
    var = var.replace(':', '-')
    new_var = ''
    if not any(elem in var for elem in ls):
        new_var = var
    else:
        for i in var:
            if i in ls:
                new_var = var.replace(i, '-')
                
    return new_var

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
                
        basket = [{"name": f.strip(),
                   "price": float(b)}
                  for f, b in 
                  zip(products, prices)]
        
        new_basket = []

        for d in basket:
            if d not in new_basket:
                new_basket.append(d)
                
        for d in new_basket:
            d["quantity"] = basket.count(d)
        
        the_date = format_date(row[0])
        dt = datetime.datetime.strptime(the_date, "%Y-%m-%d %H-%M-%S")   
        day = datetime.datetime.strftime(dt, "%Y-%m-%d")
        time = datetime.datetime.strftime(dt, "%H:%M:%S")
        transformed = {}
        transformed["date"] = day
        transformed["time"] = time
        transformed["branch"] = row[1]
        transformed["basket"] = new_basket
        transformed["payment type"] = row[3]
        transformed["total"] = float(row[4])
            
        list_to_append_to.append(transformed)
    
    
transform_data(extract.customers_list, clean_data)

pprint.pprint(clean_data[0])

