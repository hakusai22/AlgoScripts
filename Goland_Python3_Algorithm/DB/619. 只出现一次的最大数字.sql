# 单一数字 是在 MyNumbers 表中只出现一次的数字。
# 找出最大的 单一数字 。如果不存在 单一数字 ，则返回 null 。

select max(num) as num
from (select num
      from MyNumbers
      group by num
      having count(*) = 1) t