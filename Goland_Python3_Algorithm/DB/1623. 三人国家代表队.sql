# 有一个国家只有三所学校，这个国家的每一个学生只会注册 一所学校。
# 这个国家正在参加一个竞赛，他们希望从这三所学校中各选出一个学生来组建一支三人的代表队。例如：
# member_A 是从 SchoolA 中选出的
# member_B 是从 SchoolB 中选出的
# member_C 是从 SchoolC 中选出的
# 被选中的学生具有不同的名字和 ID（没有任何两个学生拥有相同的名字、没有任何两个学生拥有相同的 ID）
# 使用上述条件，编写一个解决方案来找到所有可能的三人国家代表队组合。

select a.student_name member_A,
       b.student_name member_B,
       c.student_name member_C
from SchoolA a,
     SchoolB b,
     SchoolC c
where a.student_id != b.student_id
  AND b.student_id != c.student_id
  AND a.student_id != c.student_id
  AND a.student_name != b.student_name
  AND b.student_name != c.student_name
  AND a.student_name != c.student_name
