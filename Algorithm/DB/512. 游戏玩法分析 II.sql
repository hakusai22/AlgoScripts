# 请编写解决方案，描述每一个玩家首次登陆的设备名称
SELECT a.player_id, a.device_id
FROM Activity a
WHERE (a.player_id, a.event_date) IN
      (SELECT player_id, min(event_date) FROM Activity GROUP BY player_id);


select player_id, device_id
from (select player_id, device_id, dense_rank() over (partition by player_id order by event_date asc) rnk
      from activity) a
where rnk = 1
