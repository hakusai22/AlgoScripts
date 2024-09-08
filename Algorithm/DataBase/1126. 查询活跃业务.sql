# 平均活动 是指有特定 event_type 的具有该事件的所有公司的 occurences 的均值。
#
# 活跃业务 是指具有 多个 event_type 的业务，它们的 occurences 严格大于 该事件的平均活动次数。
#
# 写一个解决方案，找到所有 活跃业务。

select business_id
from (select a.*,
             avg(occurences) over (partition by event_type) as avg_oc
      from Events a) t
where occurences > avg_oc

group by business_id
having count(distinct event_type) >= 2