# 编写一个解决方案来报告所有拥有最多员工的 项目。

select project_id
from (select project_id,
             dense_rank() over (order by count(employee_id) desc) as rnk
      from Project
      group by project_id) t
where rnk = 1
