MOD = int(1e9 + 7)
INF = int(1e20)
INFMIN = float('-inf')
INFMAX = float('inf')

if __name__ == '__main__':
    a1 = [1] * 234
    print(len(a1))

    a1.append(234)
    print(a1.count(1))

    print(a1)

    a1.clear()
    a1.extend([3214,213423,2314])

    a1.insert(1,234)
    a1.append(234234)
    print(a1)
    a1.reverse()
    a1.pop()
    print(a1)

