# 请写一个 SQL 语句，查询每一个项目中员工的 平均 工作年限，精确到小数点后两位。
select project_id,
       ROUND(avg(experience_years), 2) as average_years
from Project a
         left join Employee b using (employee_id)
group by project_id