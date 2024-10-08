import requests
from paypal.authorization import get_test_http_headers
# -*- coding: utf-8 -*-
# @Author  : yinpeng
# @Time    : 2024/03/05 21:16

if __name__ == '__main__':

    data = '{ "url": "www.xxx.com", "event_type": "BILLING.SUBSCRIPTION.CREATED", "resource_version": "1.0" }'
    response = requests.post('https://api-m.sandbox.paypal.com/v1/notifications/simulate-event', headers=get_test_http_headers(), data=data)
    print(response.status_code)
    print(response.text)