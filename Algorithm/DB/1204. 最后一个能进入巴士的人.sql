# 有一队乘客在等着上巴士。然而，巴士有1000  千克 的重量限制，所以其中一部分乘客可能无法上巴士。
# 编写解决方案找出 最后一个 上巴士且不超过重量限制的乘客，并报告 person_name 。题目测试用例确保顺位第一的人可以上巴士且不会超重。

select
    person_name
from
    (select
         turn,
         person_name,
         sum(weight) over(order by turn) as cumu_weight
     from Queue) t
where cumu_weight <= 1000
order by turn desc
limit 1

