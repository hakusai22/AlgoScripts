# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/8/10 00:20

import redis

if __name__ == '__main__':
    client = redis.Redis(host='127.0.0.1', port=6379, password='')
    client.set('username', 'admin')

    client.hset('student', 'name', 'luohao')
    client.hset('student', 'age', 40)
    keys = client.keys('*')
    print(keys)
    print(client.get('username'))
    print(client.hgetall('student'))
