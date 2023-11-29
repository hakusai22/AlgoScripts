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

