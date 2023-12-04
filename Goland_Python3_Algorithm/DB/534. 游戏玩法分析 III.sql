# 编写一个解决方案，同时报告每组玩家和日期，以及玩家到 目前为止 玩了多少游戏。
# 也就是说，玩家在该日期之前所玩的游戏总数。详细情况请查看示例。
select player_id,
       event_date,
       sum(games_played) over (partition by player_id order by event_date asc) as games_played_so_far
from Activity