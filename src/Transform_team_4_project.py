import datetime

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
    print('transform function start')
    for row in list_to_read_from:
        if len(row) == 7:
            row.pop(-1)
        row.pop(2)
        
        order = row[2].split(',')
        
        products = []
        prices = []
        
        # remove whitespace in orders from comma before splitting on comma
        for i in order:
            if i == '':
                order.remove(i)
        row[2] = ','.join(order)
       
        # putting all prices in each order, into a list
        for i in row[2].split(','):
            for j in i.split('-'):
                if is_number(j):
                    prices.append(j.strip())
            
        # removing numbers and other symbols from row[2] in order to get each product
        for i in row[2]:
            if is_number(i) or i in ['-', '.']:
                row[2] = row[2].replace(i, '')
         
            
        # putting products in products list
        for i in row[2].split(','):
            if i != '':
                products.append(i.strip())
       
        # creating basket from products and prices lists        
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

        dt = ''
        
        date_transform = False
        # had to change the formatting to remove the seconds 
        # as these new csv files have only hour and minute in time
        try:
            dt = datetime.datetime.strptime(the_date, "%d-%m-%Y %H-%M")
            date_transform = True
            
        except:
            pass
        
        try:
            dt = datetime.datetime.strptime(the_date, "%Y-%m-%d %H-%M")
            date_transform = True
        except:
            pass
        
        try:
            dt = datetime.datetime.strptime(the_date, "%m-%Y-%d %H-%M")
            date_transform = True
        except:
            pass
        
        if date_transform == True:
            day = datetime.datetime.strftime(dt, "%Y-%m-%d")
            time = datetime.datetime.strftime(dt, "%H:%M:%S")
            transformed = {}
            transformed["date"] = day
            transformed["time"] = time
            transformed["branch"] = row[1]
            transformed["basket"] = new_basket
            transformed["payment type"] = row[4]
            transformed["total"] = float(row[3])
                
            list_to_append_to.append(transformed)
    


