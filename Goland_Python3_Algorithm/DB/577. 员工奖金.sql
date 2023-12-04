# 编写解决方案，报告每个奖金 少于 1000 的员工的姓名和奖金数额。
select a.name, b.bonus
from Employee a
         left join Bonus b using (empId)
where bonus < 1000
   or bonus is null