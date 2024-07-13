from itertools import pairwise
MOD = int(1e9 + 7)
INF = int(1e20)
INFMIN = float('-inf')
INFMAX = float('inf')

if __name__ == '__main__':
    """
    python 3.10.0版本
    """
    a = pairwise('12345')
    # 输出的a应为是 12 23 34 45
    print(a)

    b = pairwise([1])
    # b为空
    print(b)

