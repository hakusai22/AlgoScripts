import base64
import json
import requests
from Python3_Basis.paypal.authorization import *



# -*- coding: utf-8 -*-
# @Author  : yinpeng
# @Time    : 2024/03/05 10:10

# https://developer.paypal.com/docs/api/webhooks/v1/#webhooks_list
if __name__ == '__main__':

    response = requests.get('https://api.paypal.com/v1/notifications/webhooks', headers=get_prod_http_headers())
    print(response.status_code)
    print(response.text)