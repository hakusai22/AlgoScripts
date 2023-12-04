# 你想知道用户在你的 app 上的访问时长情况。
# 因此你决定统计访问时长区间分别为 "[0-5>"，"[5-10>"，"[10-15>" 和 "15 minutes or more" 的会话数量，
# 并以此绘制柱状图。
#
# 写一个解决方案来报告 (bin, total) 。


select '[0-5>' bin, sum(if(duration<300,1,0)) TOTAL from Sessions
union
select '[5-10>', sum(if(300<=duration and duration<600,1,0))  from Sessions
union
select '[10-15>', sum(if(600<=duration and duration<900,1,0))  from Sessions
union
select '15 or more', sum(if(900<=duration,1,0))  from Sessions
