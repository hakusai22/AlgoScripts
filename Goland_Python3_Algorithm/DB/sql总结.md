## 常见写法
- order by count(*)
-  or bonus is null

## 常见函数

- ifnull(xx,0)
- round(xx,2)
- min() 
- max() 
- avg()
- count()
- sum(if(action = 'answer', 1, 0))
- date_add(xxx, interval 1 day)
- cast(rn as signed) --待解释

## 开窗函数  https://zhuanlan.zhihu.com/p/637159855
> 它能够让我们在不修改原有语句输出结果的基础上，直接添加新的聚合字段。

window_function_name 函数可以是聚合函数或者非聚合函数。MySQL8 支持以下几类窗口函数，

  序号函数：用于为窗口内的每一行生成一个序号，例如 ROW_NUMBER()，RANK()，DENSE_RANK() 等。
  分布函数：用于计算窗口内的每一行在整个分区中的相对位置，例如 PERCENT_RANK()，CUME_DIST() 等。
  前后函数：用于获取窗口内的当前行的前后某一行的值，例如 LAG()，LEAD() 等。
  头尾函数：用于获取窗口内的第一行或最后一行的值，例如 FIRST_VALUE()，LAST_VALUE() 等。
  聚合函数：用于计算窗口内的某个字段的聚合值，例如 SUM()，AVG()，MIN()，MAX() 等。

- sum(xxx) over(partition by xxx order by xxx)
- row_number() over (partition by xxx order by xxx)
  - row_number() ，排序不会连续执行
- dense_rank() over (order by count(xxx) des函数会把要求排序的值相同的归为一组且每组序号一样c) as rnk ... where rnk = 1
  - dense_rank() 排序是连续的，也会把相同的值分为一组且每组排序号一样
- ntile(2) OVER(order by xxx)
  - Ntile(group_num) 将所有记录分成group_num个组，每组序号一样