# 编写 SQL 语句，查询每个大箱子中苹果和橘子的个数。如果大箱子中包含小盒子，还应当包含小盒子中苹果和橘子的个数。

select sum(apple_count)  as apple_count,
       sum(orange_count) as orange_count
from (select c.apple_count,
             c.orange_count
      from Boxes b,
           Chests c
      where b.chest_id = c.chest_id
      union all
      select b.apple_count, b.orange_count
      from Boxes b) tmp
