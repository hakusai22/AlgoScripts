# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/6/17 16:39

import requests

import pytesseract
from PIL import Image  # 图形处理的库
import json
import base64

if __name__ == '__main__':
    count = 1
    while True:
        headers = {
            "Content-Type": "application/json; charset=UTF-8",
            "Referer": "https://www.hikyun.com/product/message",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
        }

        url = 'https://www.hikyun.com/webapi/portalmgr/portalweb/v1/verify/get'
        s = json.dumps({"height": "50", "width": "150"})
        r = requests.post(url, data=s, headers=headers)
        print(r.text)

        result = json.loads(r.text)
        img_str = result['data']

        print(img_str['base64ImageVerifyCode'])  # 调试时可以打开，来判断出错误的位置
        base64ImageVerifyCode = img_str['base64ImageVerifyCode']
        verifyCodeId = img_str['verifyCodeId']
        print(verifyCodeId)

        img_data = base64.b64decode(base64ImageVerifyCode)
        print(img_data)
        with open('001.jpg', 'wb') as f:
            f.write(img_data)
        print('successful')

        img2 = Image.open('001.jpg')
        gray = img2.convert('L')
        bw = gray.point(lambda x: 0 if x < 140 else 255, '1')  # 如果RGB数值小于140的变成1，否则是255。也就是将验证码背景变成白色，具体字符变成黑色。
        bw.save('aa.jpg')
        vcode = pytesseract.image_to_string(bw).replace(' ', '')

        print(vcode)
        vcode = "".join(list(filter(str.isdigit, vcode)))
        print(vcode)

        headers2 = {
            "Content-Type": "application/json; charset=UTF-8",
            "Referer": "https://www.hikyun.com/product/message",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
        }

        url2 = 'https://www.hikyun.com/webapi/portalmgr/portalweb/v1/consult/save'
        s2 = json.dumps({
            "name": "张三",
            "phone": "0571-87006061",
            "enterprise": "张三",
            "position": "TECHNICAL_MANAGER",
            "scale": "LEVEL_TWO",
            "industry": "EXPRESSWAY",
            "content": "张三",
            "verifyCode": vcode,
            "verifyCodeId": verifyCodeId
        })
        r = requests.post(url2, data=s2, headers=headers2)
        print(r.text)
        result = json.loads(r.text)
        print(result)
        print(result['code'])
        if result['code'] == 200:
            count += 1
            print("count:" + count)
