with popular as 
( select
	purchase_product_table.branch_id, 
    purchase_product_table.product_id,
    products_table.product_name, 
    sum(purchase_product_table.amount), 
    ROW_NUMBER() OVER(PARTITION BY purchase_product_table.branch_id order by sum(purchase_product_table.amount) desc) as rank
from 
	purchase_product_table
join 
	products_table 
    on 
        purchase_product_table.product_id = products_table.product_id
group by 
	purchase_product_table.branch_id, purchase_product_table.product_id, products_table.product_name
order by
	branch_id )
    
    select 
    	branch_table.branch_location,
        popular.product_name as most_popular_product, 
        popular.sum as sum_at_branch
    from
    	popular
    join
    	branch_table 
        on 
            branch_table.branch_id = popular.branch_id
    where
    	rank = 1
    order by
    	sum_at_branch desc