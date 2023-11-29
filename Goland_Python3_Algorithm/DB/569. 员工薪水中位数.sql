SELECT
    Id,Company,Salary
FROM
    (
        SELECT
            Id,Company,Salary,
            row_number() over (partition by Company order by Salary)as ranking,
            count(Id) over (partition by Company)as n
        FROM
            Employee
    )a
WHERE
        ranking>=n/2 and ranking<=n/2+1;

