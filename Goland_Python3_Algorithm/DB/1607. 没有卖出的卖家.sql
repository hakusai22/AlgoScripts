# 写一个解决方案, 报告所有在 2020 年度没有任何卖出的卖家的名字。
# 返回结果按照 seller_name 升序排列

select seller_name
from Seller t2
         left join Orders t1
                   using (seller_id)
group by t2.seller_name
having sum(if(sale_date like '2020%', 1, 0)) = 0
order by t2.seller_name

