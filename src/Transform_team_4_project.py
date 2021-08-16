import Extract_team_4_project as extract
import pprint

removed_sensitive_data = []

for row in extract.customers_list:
    row.pop(2)
    row.pop(-1)
    removed_sensitive_data.append(row)


# removing extra commas in place, in the order column
for row in removed_sensitive_data:
    order = row[2].split(',')

    for i in order:
        if i == '':
            order.remove(i)
    row[2] = ','.join(order)





