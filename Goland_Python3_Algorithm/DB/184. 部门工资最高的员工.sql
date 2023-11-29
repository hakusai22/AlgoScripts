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

