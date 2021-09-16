select
    purchase_product_table.product_id, 
    products_table.product_name, 
    SUM(amount) as total_between_1st_to_14th
from
    purchase_product_table
join
    products_table 
    on 
        purchase_product_table.product_id = products_table.product_id
where
    purchase_date between '2021-09-01' and '2021-09-14'
group by
    purchase_product_table.product_id,
    products_table.product_name,
    amount
order by
    sum(amount) desc

