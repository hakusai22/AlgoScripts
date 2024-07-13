# 查找出每个部门中薪资最高的员工。
# 按 任意顺序 返回结果表。
# 查询结果格式如下例所示。

SELECT
    d.name Department,
    e.name Employee,
    Salary
FROM
    Employee e
        JOIN
    Department d ON e.DepartmentId = d.Id
WHERE
        (e.DepartmentId , Salary) IN
        (   SELECT
                DepartmentId, MAX(Salary)
            FROM
                Employee
            GROUP BY DepartmentId
        )
;

