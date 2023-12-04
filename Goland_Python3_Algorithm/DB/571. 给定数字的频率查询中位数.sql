# 中位数 是将数据样本中半数较高值和半数较低值分隔开的值。
# 编写解决方案，解压 Numbers 表，报告数据库中所有数字的 中位数 。结果四舍五入至 一位小数 。
# 返回结果如下例所示。

select round(avg(num), 1) as median
from (select a.*,
             sum(frequency) over (order by num)      as rnk1,
             sum(frequency) over (order by num desc) as rnk2,
             sum(frequency) over ()                  as s
      from Numbers a) tmp
where rnk1 >= s / 2
  and rnk2 >= s / 2
