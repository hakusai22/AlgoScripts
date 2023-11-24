```bash
    @functools.lru_cache(None) 记忆化搜索
    字符串切片 str[::-1] # 字符串翻转  str[0:1]  左闭右开
    列表 l.append(1) l.extend([1,2,3]) l.insert(1,3) l.remove(1),(del list[0]) ,l.pop() ,l.pop(0), l.sort(reverse=True) ,l.reverse() 列表操作 
    ASCII ord('a'), chr(98), /ASCII字符数值/数值ASCII字符
    字符串 s.lower(), s.upper() ,s.title() /小写/大写/首字母大写
    字符串 str.replace('k','8',2) ,str.strip() ,str.rstrip(), str.lstrip(),  #将字符串里的k替换为8,前两个/删除空白
    字符串 str.startswith(s), str.endswith(s), str.find(s), str.index(s), str.count(s)  字符串是否以s开始的/字符串是否以s结尾的/查找s返回的是索引/获取s的索引
    字符串 s.isalpha(), s.isdigit(), s.isspace(), "_".join([1,2])  判断是否全为字符/判断是否全为数字/判断是否为空格/使用_拼接列表
    字典 m.keys(), m.values(), m.items() 字段key的列表/value的列表/ key,value值对
    eval("1,2,3") 字符串转换成列表、元组或者字典/
    公式 gcd(a,b), lcm(a,b), pow(a,b), sqrt(x), ceil(x), floor(x) /最大公约数/最小公倍数/ x的y次方/ x的平方根 /向上/向下
    堆 heapfiy([]),heappush(1), heappop(),nlargest(3,list),nsmallest(3,list),heapreplace(list,4) list转为最小堆/添加元素/弹出最小值并返回/返回堆最大的3个元素/返回堆中最小的3个元素/弹出堆顶元素,压入4
    双端队列 d.append(1), appendleft(1), d.pop(), d.popleft(), d.clear(),d.count(1), d.reverse() /队尾添加/队头添加
    栈(列表) s.append(1) s.pop() /压栈/弹出栈顶元素
    
    列表推倒式 [i for i in range(100) if i % 3 == 0] 可切片,可索引,可重复
    字典推倒式 {key: len(key) for key in list}
    集合推倒式 {i ** 2 for i in (1, 2, 3) if i % 3 == 0}  不可索引,不可切片,不可重复元素
```

```python3
def I():
    return input()

def II():
    return int(input())

def FI():
    return float(input())

def MII():
    return map(int, input().split())

def MFI():
    return map(float, input().split())

def LI():
    return list(input().split())

def LMII():
    return list(map(int, input().split()))

def LMFI():
    return list(map(float, input().split()))

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```