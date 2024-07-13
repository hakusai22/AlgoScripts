# 编写解决方案，以获取 Sales 表中所有 sale_id 对应的 product_name 以及该产品的所有 year 和 price 。

select p.product_name,
       s.year,
       s.price
from Sales s
         left join Product p
                   on s.product_id = p.product_id
