# 编写解决方案，选出每个售出过的产品 第一年 销售的 产品 id、年份、数量 和 价格。

select product_id, year as first_year,quantity,price
from Sales where (product_id,year)in (select product_id,min(year) from Sales group by product_id)