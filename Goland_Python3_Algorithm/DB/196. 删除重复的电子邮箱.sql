# 编写解决方案 删除 所有重复的电子邮件，只保留一个具有最小 id 的唯一电子邮件。

delete
from Person
where id in (select id
             from (select id, dense_rank() over (partition by email order by id) as rk from Person) tmp
             where rk != 1)