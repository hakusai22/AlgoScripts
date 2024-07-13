# 编写解决方案，找出每位学生获得的最高成绩和它所对应的科目，
#
# 若科目成绩并列，取 course_id 最小的一门。
# 查询结果需按 student_id 增序进行排序。

select student_id, min(course_id) as course_id, grade
from Enrollments
where (student_id, grade) in (select student_id, max(grade) from Enrollments student_id group by student_id)
group by student_id
order by student_id