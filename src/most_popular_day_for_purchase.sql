select
    To_Char(purchase_date, 'DAY') as day,
    sum(purchase_total) as total_amount_for_day
from
    purchase_table
where
    purchase_date between '2021-09-01' and '2021-09-08'
group by
    day
order by
    sum(purchase_total) desc
