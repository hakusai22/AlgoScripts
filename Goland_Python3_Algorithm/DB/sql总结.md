## 常见写法
- order by count(*)

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

## 开窗函数

- sum(xxx) over(partition by xxx order by xxx)
- row_number() over (partition by xxx order by xxx)
  - row_number() 函数会把要求排序的值相同的归为一组且每组序号一样，排序不会连续执行
- dense_rank() over (order by count(xxx) desc) as rnk ... where rnk = 1
  - dense_rank() 排序是连续的，也会把相同的值分为一组且每组排序号一样
- ntile(2) OVER(order by xxx)
  - Ntile(group_num) 将所有记录分成group_num个组，每组序号一样