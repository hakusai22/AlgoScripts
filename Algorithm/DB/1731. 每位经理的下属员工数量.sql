# 写SQL查询需要听取汇报的所有经理的ID、名称、直接向该经理汇报的员工人数，以及这些员工的平均年龄，
# 其中该平均年龄需要四舍五入到最接近的整数。

select
    t2.employee_id,
    t2.name,
    count(t1.employee_id) as reports_count,
    round(avg(t1.age)) as average_age
from Employees t1, Employees t2
where t1.reports_to = t2.employee_id
group by t2.employee_id
order by t2.employee_id

