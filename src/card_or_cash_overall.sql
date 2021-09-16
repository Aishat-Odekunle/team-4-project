select 
    payment_type, 
    count(payment_type) as number_of_customers_used
from 
    purchase_table 
group by 
    payment_type 
order by 
    count(payment_type) desc;
