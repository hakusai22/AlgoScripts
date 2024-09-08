# 一个员工可以属于多个部门。当一个员工加入超过一个部门的时候，
# 他需要决定哪个部门是他的直属部门。请注意，
# 当员工只加入一个部门的时候，那这个部门将默认为他的直属部门，虽然表记录的值为'N'.
# 请编写解决方案，查出员工所属的直属部门。


SELECT employee_id, department_id
FROM Employee
GROUP BY employee_id
HAVING COUNT(primary_flag) = 1
UNION
SELECT employee_id, department_id
FROM Employee
WHERE primary_flag = 'Y'

