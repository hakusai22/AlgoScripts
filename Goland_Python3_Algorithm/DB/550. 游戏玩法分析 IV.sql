# 编写解决方案，报告在首次登录的第二天再次登录的玩家的 比率，四舍五入到小数点后两位。
# 换句话说，你需要计算从首次登录日期开始至少连续两天登录的玩家的数量，然后除以玩家总数。
select ifnull(
               round(
                           count(distinct player_id) /
                           (select count(distinct player_id) from activity)
                   , 2)
           , 0) as fraction
from activity
where (player_id, event_date) in
      (select player_id, date_add(min(event_date), interval 1 day)
       from activity
       group by player_id)

