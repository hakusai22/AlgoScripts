# 编写一个解决方案，找出至少有五个直接下属的经理。
select Employee.Name as Name
from Employee
where id in (select ManagerId as Id
             from Employee
             group by ManagerId
             having count(Id) >= 5)

