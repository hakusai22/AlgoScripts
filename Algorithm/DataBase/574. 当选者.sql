# 编写解决方案来报告获胜候选人的名字(即获得最多选票的候选人)。
#
# 生成的测试用例保证 只有一个候选人赢得 选举。

select name
from Candidate
where id = ((select candidateId
             from Vote
             group by candidateId
             order by count(*) desc
             limit 1))