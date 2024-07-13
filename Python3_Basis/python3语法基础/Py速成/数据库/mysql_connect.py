# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/8/15 21:47

import pymysql

try:
    con = pymysql.connect(host='127.0.0.1', port=3306,
                          user='root', password='12345678',
                          database='hrs', charset='utf8mb4')
    # 获取数据
    cursor = con.cursor()
    cursor.execute('SELECT * FROM `news`')
    rest = cursor.fetchone()
    print(rest)

    # 关闭连接
    con.close()
except pymysql.Error as e:
    print("MysqlError: %s" % e)
