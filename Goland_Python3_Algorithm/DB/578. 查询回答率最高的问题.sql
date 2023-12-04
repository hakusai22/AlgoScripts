# 回答率 是指：同一问题编号中回答次数占显示次数的比率。
# 编写一个解决方案以报告 回答率 最高的问题。如果有多个问题具有相同的最大 回答率 ，返回 question_id 最小的那个。

select question_id as survey_log
from SurveyLog
group by question_id
order by sum(if(action = 'answer', 1, 0)) / sum(if(action = 'show', 1, 0)) desc, question_id
limit 1
