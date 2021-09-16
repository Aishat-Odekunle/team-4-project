with busiest_hour as 
    (select branch_table.branch_location, 
    purchase_table.branch_id, 
    extract(hour from purchase_time) as the_hour, 
    sum(purchase_total),
    ROW_NUMBER() OVER(PARTITION BY purchase_table.branch_id order by sum(purchase_total) desc) as rank
    from 
        purchase_table
    join 
        branch_table ON purchase_table.branch_id = branch_table.branch_id
    group by 
        purchase_table.branch_id,
        the_hour, 
        branch_table.branch_location)

    select 
        branch_location,
        the_hour,
        round(sum) as total_spent_per_hour
    from
        busiest_hour
    where 
        rank = 1
    order by 
        sum desc
