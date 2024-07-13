
# 找出那些 没有被 id = 2 的客户 推荐 的客户的姓名。
select name
from Customer
where referee_id != 2
   or referee_id is null