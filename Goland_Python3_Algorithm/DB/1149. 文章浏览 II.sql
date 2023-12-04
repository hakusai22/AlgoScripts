# 编写解决方案来找出在同一天阅读至少两篇文章的人。

select distinct viewer_id as id
from Views
group by view_date, viewer_id
having count(distinct article_id) >= 2
order by id