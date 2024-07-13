# 每年，学校会公布学生申请所需的最低分数要求。学校根据所有学生的考试成绩来决定其最低分数要求。
#
# 学校希望确保即使 每 一个满足分数要求的学生都申请该学校，学校也有足够的能力接纳每一个学生。
# 学校也希望 尽可能多 的学生能申请该学校。
# 学校 必须 使用在 Exam 表中的 score 来作为最低分数要求。
# 编写一个解决方案，报告每所学校的 最低分数要求。如果同时有多个 score 值满足上述要求，则选择其中 最小的一个。如果数据不足以决定 最低分数要求，那么输出 -1。

select school_id,
       ifnull(min(score), -1) score
from schools
         left join exam
                   on capacity >= student_count

group by school_id
