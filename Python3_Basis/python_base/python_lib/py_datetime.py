# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/6/26 17:11
import datetime as dt

if __name__ == '__main__':
    print(dt.date(2007, 9, 25))  # 2007-09-25

    d1 = dt.date(2008, 9, 25)

    d2 = dt.date(2007, 9, 25)

    print(d1.strftime('%A, %m/%d/%y'))  # Thursday, 09/25/08
    print(d1.strftime('%a, %m-%d-%Y'))  # Thu, 09-25-2008

    print(d2 - d1)  # -366 days, 0:00:00

    t1 = dt.time(15, 38)
    t2 = dt.time(18)
    print(t1)  # 15:38:00
    print(t2)  # 18:00:00

    print(t1.strftime('%H:%M:%S, %p'))  # 15:38:00, PM

    print(dt.datetime(2022, 3, 7, 2, 49, 39))  # 2022-03-07 02:49:39
    print(dt.datetime.now())  # 2022-06-26 17:28:06.825796

    print(d1 + dt.timedelta(30))  # 将当前时间加上30天：

    # %a	星期英文缩写
    # %A	星期英文
    # %w	一星期的第几天，[0(sun),6]
    # %b	月份英文缩写
    # %B	月份英文
    # %d	日期，[01,31]
    # %H	小时，[00,23]
    # %I	小时，[01,12]
    # %j	一年的第几天，[001,366]
    # %m	月份，[01,12]
    # %M	分钟，[00,59]
    # %p	AM 和PM
    # %S	秒钟，[00,61]
    # %U	一年中的第几个星期，星期日为第一天，[00,53]
    # %W	一年中的第几个星期，星期一为第一天，[00,53]
    # %y	没有世纪的年份
    # %Y	完整的年份
