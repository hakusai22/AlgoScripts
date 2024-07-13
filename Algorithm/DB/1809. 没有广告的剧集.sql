# 编写解决方案找出所有没有广告出现过的剧集。

select session_id
from playback
where session_id not in (
    select distinct session_id
    from playback p join ads a
                         on p.customer_id=a.customer_id
    where timestamp between start_time and end_time
)

