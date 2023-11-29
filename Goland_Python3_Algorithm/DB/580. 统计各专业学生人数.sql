# Write your MySQL query statement below
# 编写一个SQL查询，为 Department 表中的所有部门(甚至是没有当前学生的部门)
# 报告各自的部门名称和每个部门的学生人数。
# 按 student_number 降序 返回结果表。如果是平局，则按 dept_name 的  字母顺序 排序。
select dept_name,(
    count(a2.dept_id)
    ) student_number
from Department a1
         left join Student a2 on a1.dept_id = a2.dept_id
group by dept_name
order by student_number desc,dept_name

