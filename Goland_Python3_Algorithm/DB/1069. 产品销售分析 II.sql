select a.product_id,
       sum(quantity) as total_quantity
from Sales as a
group by a.product_id