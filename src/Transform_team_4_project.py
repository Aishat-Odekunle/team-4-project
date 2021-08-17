import Extract_team_4_project as extract


removed_sensitive_data = []

def transform_data(list_to_read_from, list_to_append_to):
    for row in list_to_read_from:
        row.pop(2)
        row.pop(-1)
        list_to_append_to.append(row)

    # removing extra commas in place, in the order column    
    for row in list_to_append_to:
        order = row[2].split(',')
        
        for i in order:
            if i == '':
                order.remove(i)
        row[2] = ', '.join(order)

transform_data(extract.customers_list, removed_sensitive_data)







