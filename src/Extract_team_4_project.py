from csv import DictReader

customers_list = []
with open('2021-02-23-isle-of-wight.csv') as cafe_file:
    cafe_list = DictReader(cafe_file)
    for cafe_items in cafe_list:
        customers_list.append(cafe_items)
        
print(customers_list)
    