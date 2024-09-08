# 编写解决方案以获取在 2020 年登录过的所有用户的本年度 最后一次 登录时间。结果集 不 包含 2020 年没有登录过的用户。

select user_id, max(time_stamp) last_stamp
from logins
where time_stamp like '2020%'
group by user_id