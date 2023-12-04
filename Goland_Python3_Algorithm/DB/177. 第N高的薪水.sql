# 查询 Employee 表中第 n 高的工资。如果没有第 n 个最高工资，查询结果应该为 null 。

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    RETURN (
        SELECT
            DISTINCT e.salary
        FROM
            employee AS e
        WHERE
                (
                    SELECT
                        COUNT(DISTINCT salary)
                    FROM
                        employee
                    WHERE
                            salary > e.salary
                ) = N - 1
    );
END
