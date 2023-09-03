### Trie树又称字典树、单词查找树。是一种能够高效存储和查找字符串集合的数据结构。

![img.png](images/img.png)

![img.png](images/img2.png)


> 插入操作代码

```python3
N = 100010
# son[p][u] 表示p节点的孩子u是否存在于矩阵
son = [[0] * 26 for _ in range(N)]
# 存储每个节点出现的次数
cnt = [0] * N
char = ['0'] * N
# idx是新需要插入的节点的编号
idx = 0

def insert(char):
    global idx
    p = 0
    for i in range(len(char)):
        # 将字母转化为数字
        u = ord(char[i]) - 97
        # 该节点不存在，创建节点,其值为下一个节点位置
        if not son[p][u]:
            idx += 1
            son[p][u] = idx
        # 使“p指针”指向下一个节点位置
        p = son[p][u]
    # //结束时的标记，也是记录以此节点结束的字符串个数
    cnt[p] += 1
```

> 查找操作代码：

```python3
    def query(c):
    global idx
    p = 0
    for i in range(len(c)):
        u = ord(c[i]) - 97
        # 该节点不存在，即该字符串不存在
        if not son[p][u]:
            return 0
        p = son[p][u]
    # 返回字符串出现的次数
    return cnt[p]
```


![img.png](img.png)

![img_1.png](img_1.png)