select group_id, player_id
from (select group_id, player_id, row_number() over (partition by group_id order by score_cnt desc,player_id asc) as r
      from (select player_id,
                   group_id,
                   sum(if(player_id = first_player, first_score, 0)) +
                   sum(if(player_id = second_player, second_score, 0)) as score_cnt
            from Players
                     join Matches
            group by player_id) as t) tt
where r = 1