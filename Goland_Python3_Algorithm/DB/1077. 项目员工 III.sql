# 编写解决方案，报告在每一个项目中 经验最丰富 的雇员是谁。
# 如果出现经验年数相同的情况，请报告所有具有最大经验年数的员工。

with t as
         (select a.project_id,
                 a.employee_id,
                 b.experience_years
          from project a
                   join employee b
                        using (employee_id))

select project_id, employee_id
from (select project_id,
             employee_id,
             dense_rank() over (partition by project_id order by experience_years desc) as rnk
      from t) tmp
where rnk = 1
