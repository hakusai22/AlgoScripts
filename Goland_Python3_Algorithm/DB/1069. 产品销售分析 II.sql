# 编写解决方案，统计每个产品的销售总量。
select a.product_id,
       sum(quantity) as total_quantity
from Sales as a
group by a.product_id