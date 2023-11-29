select name
from Candidate
where id = ((select candidateId
             from Vote
             group by candidateId
             order by count(*) desc
             limit 1))