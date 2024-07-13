# 编写解决方案，找出从今天起最多 90 天内，每个日期该日期首次登录的用户数。假设今天是 2019-06-30 。

select first_date     as login_date,
       count(user_id) as user_count
from (select user_id,
             min(activity_date) as first_date
      from Traffic
      where activity = 'login'
      group by user_id) t
where datediff("2019-06-30", first_date) <= 90
group by login_date