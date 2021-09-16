select
    purchase_table.branch_id, 
    branch_table.branch_location, 
    SUM(purchase_total) as revenue
from
    purchase_table
join
    branch_table ON purchase_table.branch_id = branch_table.branch_id
where
    purchase_date BETWEEN '2021-09-01' AND '2021-09-14'
group by
    purchase_table.branch_id,
    branch_table.branch_location
order by
    sum(purchase_total) desc
