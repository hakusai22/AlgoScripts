# 查询并返回 Employee 表中第二高的薪水 。
# 如果不存在第二高的薪水，查询应该返回 null(Pandas 则返回 None) 。
select ifnull((select distinct salary as SecondHighestSalary
               from Employee
               order by salary desc
               limit 1,1), null) as SecondHighestSalary;


select (select distinct salary
        from (select a.*, dense_rank() over (order by salary desc) as rnk
              from Employee a) t
        where rnk = 2) SecondHighestSalary
