# 编写解决方案报告 2016 年 (tiv_2016) 所有满足下述条件的投保人的投保金额之和：
#
# 他在 2015 年的投保额 (tiv_2015) 至少跟一个其他投保人在 2015 年的投保额相同。
# 他所在的城市必须与其他投保人都不同（也就是说 (lat, lon) 不能跟其他任何一个投保人完全相同）。
# tiv_2016 四舍五入的 两位小数 。

select
    round(sum(tiv_2016), 2) as tiv_2016
from
    Insurance
where pid in (
    select
        pid
    from
        Insurance
    group by lat, lon
    having count(1) = 1
) and pid not in (
    select
        pid
    from
        Insurance
    group by tiv_2015
    having count(1) = 1
)

