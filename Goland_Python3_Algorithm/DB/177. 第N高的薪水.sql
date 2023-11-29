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
