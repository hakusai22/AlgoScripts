# 编写一个解决方案，找出在 2019-08-16 时全部产品的价格，假设所有产品在修改前的价格都是 10 。
with cte1 as
         (select distinct product_id
          from Products),


     cte2 as
         (select product_id,
                 new_price
          from Products
          where (product_id, change_date) in
                (select product_id,
                        max(change_date)
                 from Products
                 where change_date <= "2019-08-16"
                 group by product_id))

### 窗口函数 ###
# cte2 as
# (
#     select
#         product_id,
#         new_price
#     from (
#         select
#             product_id,
#             new_price,
#             dense_rank() over(partition by product_id
#                             order by change_date desc) as rnk
#         from Products
#         where change_date <= '2019-08-16'
#     ) t
#     where rnk = 1
# )

select a.product_id,
       ifnull(new_price, 10) as price
from cte1 a
         left join cte2 b
                   using (product_id)
