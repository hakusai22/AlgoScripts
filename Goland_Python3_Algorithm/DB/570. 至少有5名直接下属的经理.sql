select Employee.Name as Name
from Employee where id in (
    select ManagerId as Id
    from Employee
    group by ManagerId
    having count(Id) >= 5
)

