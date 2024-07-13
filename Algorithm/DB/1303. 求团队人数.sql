# 编写解决方案以求得每个员工所在团队的总人数。

select employee_id, count(*) over(partition by team_id) team_size
from Employee