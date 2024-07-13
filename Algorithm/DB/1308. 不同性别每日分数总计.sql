# 编写解决方案统计每种性别在每一天的总分。
# 返回按 gender 和 day 对查询结果 升序排序 的结果。

select gender, day, sum(score_points) over (partition by gender order by day) total
from scores
order by gender, day