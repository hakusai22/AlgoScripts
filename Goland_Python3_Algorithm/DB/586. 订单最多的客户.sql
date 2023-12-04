# 查找下了 最多订单 的客户的 customer_number 。
# 测试用例生成后， 恰好有一个客户 比任何其他客户下了更多的订单。
# 查询结果格式如下所示。

select customer_number
from Orders
group by customer_number
order by count(*) desc
limit 1