# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/8/11 22:18
import random

import pymysql

def insert(num):
    db = pymysql.connect(host='xxxx', port=3306,
                         user='xxx', password='xxxx',
                         database='xxx', charset='utf8mb4')
    cursor = db.cursor()
    for i in range(num):
        time = random.randint(1658937600, 1758937600)
        userId = random.randint(300152507, 390152507)
        try:
            cursor.execute(
                "insert into period_info(userId,insertTimestamp,flag) values('{}','{}','{}')".format(userId, time, 0))
            db.commit()
        except Exception as e:
            print("第{}条数据插入失败！原因：{}".format(i, e))
        else:
            print("第{}条数据插入成功！".format(i))
        finally:
            pass
    db.close()

if __name__ == "__main__":
    insert(100000)
