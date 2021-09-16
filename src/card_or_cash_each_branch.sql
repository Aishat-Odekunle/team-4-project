with c as 
    (select
        branch_table.branch_location,
        purchase_table.payment_type,
        count(purchase_table.payment_type) as number_of_customers_used,
        ROW_NUMBER() OVER(PARTITION BY purchase_table.branch_id order by purchase_table.payment_type) as rank
    from
        purchase_table
    join
        branch_table 
        on 
            branch_table.branch_id = purchase_table.branch_id
    group by
        purchase_table.payment_type,
        branch_table.branch_location,
        purchase_table.branch_id
    order by 
        purchase_table.branch_id )
    
    select
        branch_location,
        payment_type,
        number_of_customers_used
    from
        c
    where
        rank = 1