from collections import defaultdict, Counter, deque, OrderedDict, namedtuple

MOD = int(1e9 + 7)
INF = int(1e20)
INFMIN = float('-inf')
INFMAX = float('inf')

if __name__ == '__main__':
    dict3 = {}

    dict3[1] = 3453
    print(dict3)
    dict3.clear() # 清空字典

    dict4 = defaultdict(int)
    print(dict4)
    dict4[1234] = 1234
    del dict4[1234]
    print(dict4[1234])

    dict1 = defaultdict(set)
    dict1["1"] = "100"

    dict2 = dict()
    dict2[2] = 1
    print(dict2)

    print(dict1["1"])
    print(dict1[1])

    str = "sadfasd"
    c = Counter(str)
    c[0] = 1
    print(c[0])
    b = OrderedDict(c)
    print(b)
    print(c)

    print(type(dict1.items()))
    print(chr(98))
