
MOD = int(1e9 + 7)
INF = int(1e20)
INFMIN = float('-inf')
INFMAX = float('inf')

if __name__ == '__main__':
    a = (b := (c := (d := 5)))
    print(a, b, c, d)
    b = 3 * (a := 4)
    print(b)
