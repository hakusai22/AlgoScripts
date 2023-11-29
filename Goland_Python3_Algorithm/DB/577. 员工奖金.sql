# Write your MySQL query statement below

select a.name,
       b.bonus
from Employee a
         left join Bonus b
                   using (empId)
where bonus < 1000
   or bonus is null