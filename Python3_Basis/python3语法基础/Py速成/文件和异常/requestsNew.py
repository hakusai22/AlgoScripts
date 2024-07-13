# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/8/8 21:28

import json

import requests


def main():
    arr = []
    i = 0
    while i < 30:
        resp = requests.get('http://api.tianapi.com/duilian/index?key=9d3d787bcd8854773cb97b8cad9628fe')
        data_model = json.loads(resp.text)
        for news in data_model['newslist']:
            arr.append(news['content'])

    print(list(arr))


if __name__ == '__main__':
    main()
