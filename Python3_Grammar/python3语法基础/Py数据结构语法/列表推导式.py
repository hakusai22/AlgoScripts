MOD = int(1e9 + 7)
INF = int(1e20)
INFMIN = float('-inf')
INFMAX = float('inf')
'''
列表推倒式 [i for i in range(100) if i % 3 == 0] 可切片,可索引,可重复
'''

if __name__ == '__main__':
    # in后面跟其他可迭代对象,如字符串
    list_c = [7 * c for c in "python"]
    print(list_c)

    # 带if条件语句的列表推导式
    list_d = [d for d in range(6) if d % 2 != 0]
    print(list_d)

    # 多个for循环
    list_e = [(i, j * j) for i in range(3) for j in range(5, 15, 5)]
    print(list_e)
    list_e1 = [[i, j * j] for i in range(3) for j in range(5, 15, 5)]
    print(list_e1)

    # 嵌套列表推导式,多个并列条件
    list_g = [[i for i in range(j - 3, j)] for j in range(22) if j % 3 == 0 and j != 0]
    print(list_g)
