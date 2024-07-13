import base64
import json
import requests
from paypal.authorization import get_test_http_headers, get_productId

# -*- coding: utf-8 -*-
# @Author  : yinpeng
# @Time    : 2024/03/05 10:54

# https://developer.paypal.com/docs/api/subscriptions/v1/#plans_get
if __name__ == '__main__':

    response = requests.get('https://api-m.sandbox.paypal.com/v1/billing/plans/P-51J87956H28500615MXSWO7I', headers=get_test_http_headers())
    print(response.status_code)
    print(response.text)
