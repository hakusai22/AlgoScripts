import requests
from Python3_Basis.paypal.authorization import *

# -*- coding: utf-8 -*-
# @Author  : yinpeng
# @Time    : 2024/03/05 10:47


if __name__ == '__main__':

    response = requests.get('https://api.paypal.com/v1/notifications/webhooks-event-types', headers=get_prod_http_headers())
    print(response.status_code)
    print(response.text)
