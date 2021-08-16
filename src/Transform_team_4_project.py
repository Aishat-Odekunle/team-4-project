import Extract_team_4_project as extract
import pprint

removed_sensitive_data = []

for row in extract.customers_list:
    row.pop(2)
    row.pop(-1)
    removed_sensitive_data.append(row)
    
pprint.pprint(removed_sensitive_data[:4])