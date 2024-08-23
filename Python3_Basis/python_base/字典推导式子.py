MOD = int(1e9 + 7)
INF = int(1e20)
INFMIN = float('-inf')
INFMAX = float('inf')
'''
字典推倒式 {key: len(key) for key in list}
'''

# 语法1
'''
	new_dictionary = {key_exp:value_exp for key, value in dict.items() if condition}
	字典推导式说明：
    key：dict.items()字典中的key
    value：dict.items()字典中的value
    dict.items()：序列
    condition：if条件表达式
    key_exp：在for循环中，如果if条件表达式condition成立(即条件表达式成立)，返回对应的key,value当作key_exp,value_exp处理 
    value_exp：在for循环中，如果if条件表达式condition成立(即条件表达式成立)，返回对应的key,value当作key_exp,value_exp处理
	这样就返回一个新的字典。
'''

# 语法2
'''
	{key_exp:value_exp1 if condition else value_exp2 for key, value in dict.items()}
	字典推导式说明：
    key：dict.items()字典中的key 
    value：dict.items()字典中的value 
    dict.items()：序列 
    condition：if条件表达式的判断内容 
    value_exp1：在for循环中，如果条件表达式condition成立(即条件表达式成立)，返回对应的key,value并作key_exp,value_exp1处理
    value_exp2：在for循环中，如果条件表达式condition不成立(即条件表达式不成立)，返回对应的key,value并作key_exp,value_exp2处理
'''

if __name__ == '__main__':
    dictionary_1 = {'a': '1234', 'B': 'FFFF', 'c': ' 23432', 'D': '124fgr', 'e': 'eeeee', 'F': 'QQQQQ'}

    # 案例一：获取字典中key值是小写字母的键值对
    new_dict_1 = {key: value for key, value in dictionary_1.items() if key.islower()}
    new_dict_2 = {g: h for g, h in dictionary_1.items() if g.islower()}
    # g, h只是一个变量，使用任意字母都行，但是一定要前后保持一致。
    print(new_dict_1)
    print(new_dict_2)

    # 案例二：将字典中的所有key设置为小写
    new_dict_3 = {key.lower(): value for key, value in dictionary_1.items()}
    # 将字典中的所有key设置为小写,value值设置为大写
    new_dict_4 = {key.lower(): value.upper() for key, value in dictionary_1.items()}
    print(new_dict_3)
    print(new_dict_4)

    # 案例三：将字典中所有key是小写字母的value统一赋值为'error'
    new_dict_5 = {key: value if not key.islower() else 'error' for key, value in dictionary_1.items()}  # if条件表达式用到了“非”的逻辑
    # value if not key.islower() else 'error' 这一段的代码的含义是：
    # 如果not key.islouer()--key值不是小写的，那么返回if前面的value值，否则就返回else后面的值。
    print(new_dict_5)

    # 将key中大小写相同的字母的value值求和
    dict_a = {'a': 2, 'B': 5, 'A': 7, 'C': 10}
    new_dict_1 = {key.lower(): dict_a.get(key.lower(), 0) + dict_a.get(key.upper(), 0) for key in dict_a.keys() if key.lower() in ['a', 'b']}
    print(new_dict_1)


    # 将字典中key、value互换位置
    d = {1: 'a', 2: 'b', 3: 'c'}
    dd = {key: value for value, key in d.items()}
    print(d)
    print(dd)

    # 将两个长度相同的列表合并成字典
    name = ['zhangsan', 'lisi', 'wangwu', 'maliu']
    sign = ['双鱼座', '天蝎座', '水瓶座', '巨蟹座']
    new_dict_2 = {name: value for name, value in zip(name, sign)}
    print(new_dict_2)
    print(type(zip(name, sign)))