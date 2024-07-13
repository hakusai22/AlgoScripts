## Python3 刷题总结

- 常用内置数据类型：list, tuple, dict, set, frozenset
- collections 模块：Counter(计数器), deque(双端队列), OrderedDict(有序字典)，defaultdict(默认值字典)
- heapq: 堆操作
- bisect: 二分查找
- 矩阵。正确初始化一个不可变对象的二维数组：dp = [ [0]*col for _ in range(row) ]
- 缓存。python3 的 functools 模块自带了 cache(等价于lru_cache(maxsize=None)) 和 lru_cache 装饰器，在一些需要递归记忆化搜索的时候会很方便
  ![img.png](img.png)

### python 递归暴栈(栈溢出)

python 递归函数默认递归深度比较小，你可以通过 sys.getrecursionlimit() 函数打印出来。 我在 mac 机器上测试的时候，以下结果 python2 输出
1000。这就导致一些递归函数测试用例稍微多一些就会报错。 (一个用例超过上千个数据就会报错了)

```python
import sys

print(sys.getrecursionlimit())  # 我的 mac 机器上输出 1000
```

可以把以下代码设置最大栈深度，放到文件开头，在牛客上提交代码的时候可以避免一些递归代码报错。 (leetcode 似乎给设置了，类似的题目发现力扣上提交不会栈溢出但是在牛客就会)

```python
import sys

sys.setrecursionlimit(100000)  # 设置函数栈深度足够大，避免栈溢出错误
```

### python list 技巧

```python
# 排序嵌套 list
l = [('a', 1), ('c', 2), ('b', 3)]
sorted(l, key=lambda p: p[0])  # 根据第1个值排序，[('a', 1), ('b', 3), ('c', 2)]
sorted(l, key=lambda p: p[1])  # 根据第2个值排序，[('a', 1), ('c', 2), ('b', 3)]
sorted(l, key=lambda p: (p[0], p[1]))  # 根据元组第0个值升序排序，若第0个值相等则根据第1个值升序排序
sorted(l, key=lambda p: (p[0], -p[1]))  # 根据元组第0个值升序排序，若第0个值相等则根据第1个值降序排序

# 同时获取最大值的下标和值
l = [1, 2, 5, 4, 3]
maxi, maxval = max(enumerate(l), key=lambda iv: iv[1])  # 2, 5

# python3 排序list自定义函数(python2 直接用 cmp 参数， python3 需要用 cmp_to_key 转成 key 参数)
from functools import cmp_to_key

nums = [3, 2, 1, 4, 5]
sorted(nums, key=cmp_to_key(lambda a, b: a - b))  # [1 ,2 ,3, 4, 5]
sorted(nums, key=cmp_to_key(lambda a, b: b - a))  # [5, 4, 3, 2, 1]

# 一行代码判断列表是否有序
issorted = all(l[i] <= l[i + 1] for i in range(len(l) - 1))

# python3 一行代码求前缀和
from itertools import accumulate

presums = list(accumulate([1, 2, 3]))  # [1, 3, 6]

matrix = [[]]
# 一行代码求矩阵元素总和 https://stackoverflow.com/questions/10713150/how-to-sum-a-2d-array-in-python
allsum = sum(map(sum, matrix))  # 或者 allsum = sum((sum(row) for row in matrix))
```

### python dict 技巧

```python
# python 根据 key，value 排序字典
d = {'d': 4, 'a': 1, 'b': 2, 'c': 3}
# dict sort by **key** and reverse
dict(sorted(d.items()))  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
dict(sorted(d.items(), reverse=True))  # {'d': 4, 'c': 3, 'b': 2, 'a': 1}

# dict sort by **value** and reverse
dict(sorted(d.items(), key=lambda kv: kv[1]))  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
dict(sorted(d.items(), key=lambda kv: kv[1], reverse=True))  # {'d': 4, 'c': 3, 'b': 2, 'a': 1}

# 获取字典对应的最大值对应的 key,value
mydict = {'A': 4, 'B': 10, 'C': 0, 'D': 87}
maximum = max(mydict, key=mydict.get)  # Just use 'min' instead of 'max' for minimum.
maxk, maxv = maximum, mydict[maximum]
# 或者
maxk, maxv = max(mydict.items(), key=lambda k: k[1])

# 支持默认值的有序字典 (OrderedDict and defaultdict)  (注意是 key 插入顺序不是字典序)
# https://stackoverflow.com/questions/6190331/how-to-implement-an-ordered-default-dict
od = OrderedDict()  # collections.OrderedDict()
i = 0
od[i] = od.get(i, 0) + 1  # 间接实现了 defaultdict(int) ，同时保持了插入字典的 key 顺序
```


> Python3 常用模版
```python
from bisect import bisect_left, bisect_right, insort_left, insort_right, insort, bisect
from math import ceil, floor, pow, gcd, sqrt, log10, fabs, fmod, factorial, inf, pi, e
from heapq import heapify, heapreplace, heappush, heappop, heappushpop, nlargest, nsmallest
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations, combinations_with_replacement, accumulate, count, groupby, pairwise
from queue import PriorityQueue, Queue, LifoQueue
from functools import lru_cache, cache, reduce
from typing import List, Optional
import sys

from sortedcontainers import SortedList, SortedDict, SortedSet

sys.setrecursionlimit(10001000)

MOD = int(1e9 + 7)
INF = int(1e20)
INFMIN = float('-inf')  # 负无穷
INFMAX = float('inf')  # 正无穷
PI = 3.141592653589793
direc = [(1, 0), (0, 1), (-1, 0), (0, -1)]
direc8 = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
ALPS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alps = 'abcdefghijklmnopqrstuvwxyz'

'''
heaqp
deque
permutations(arr,r) 返回的是一个长度为 r 的所有可能排列，无重复元素
combinations(arr,r) 返回的是一个长度为r的组合，它是有序的，无重复元素
bisect_left()等同 函数返回排序数组中值等于k的最左索引，如果没有，就返回插入后其索引
bisect()和bis_right函数返回排序数组中值等于k的最右索引+1，如果没有，就返回插入后其索引
gcd(), ord(), chr(), lower(), upper() 最大公约数/ASCII字符数值/数值ASCII字符/小写/大写
startswith(s), endswith(s), find(), index(), count(s)  字符串是否以s开始的/字符串是否以s结尾的/查找返回的是索引/获取索引
isalpha(), isdigit(), space(),join()  判断是否全为字符/判断是否全为数字/判断是否为空格/拼接
eval() 字符串转换成列表、元组或者字典/
uniform(x, y), pow(x, y)# 随机生成下一个实数，它在[x,y]范围内/ x**y 运算后的值。
字典推倒式 {key: len(key) for key in list}
列表推倒式 [i for i in range(100) if i % 3 == 0] 可切片,可索引,可重复
集合推倒式 {i ** 2 for i in (1, 2, 3)}  不可索引,不可切片,不可重复元素
'''

# 数值和字母进行转换 ord()函数是把字符转换成ASCII码 chr()函数是把ASCII码转换成字符
def alp(i):
    return chr(ord('a') + i % 26)  # i=0->'a', i=25->'z'

# lcm 最小公倍数 gcd 最大公约数
def lcm(x, y):
    return x * y // gcd(x, y)

# 快速幂
def qpow(x, y):
    ans = 1
    while y:
        if y & 1:
            ans *= x
        x *= x
        y >>= 1
    return ans

# 求组合数
def Comb(n, m, p):
    a = (factorial(n)) % p
    b = (qpow(factorial(m), (p - 2), p)) % p
    c = (qpow(factorial(n - m), (p - 2), p)) % p
    return a * b * c % p

# lucas求组合数
def Lucas(n, m, p):
    if m == 0:
        return 1
    return Comb(n % p, m % p, p) * Lucas(n // p, m // p, p) % p

```


```python
# 编写链表题目经常用到的一些通用函数和调试函数，定义等，方便代码调试

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return 'Node({})'.format(self.val)

    # 用来输出调试
    __repr__ = __str__

# 缩写，单测方便写，比如构建链表 1->2->3  N(1, N(2, N(3)))
N = Node = ListNode

def to_list(head):
    """linked list to python []"""
    res = []
    curnode = head
    while curnode:
        res.append(curnode.val)
        curnode = curnode.next
    return res

def gen_list(nums):
    """用数组生成一个链表方便测试 [1,2,3] 1->2->3
    """
    if not nums:
        return None
    head = ListNode(nums[0])
    pre = head
    for i in range(1, len(nums)):
        node = ListNode(nums[i])
        pre.next = node
        pre = node
    return head

def print_list(head):
    """打印链表"""
    cur = head
    res = ""
    while cur:
        res += "{}->".format(cur.val)
        cur = cur.next
    res += "nil"
    print(res)
```