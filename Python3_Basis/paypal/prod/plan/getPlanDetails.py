import base64
import json
import requests
from Python3_Basis.paypal.authorization import *

# -*- coding: utf-8 -*-
# @Author  : yinpeng
# @Time    : 2024/03/05 10:54

# https://developer.paypal.com/docs/api/subscriptions/v1/#plans_get
if __name__ == '__main__':

    response = requests.get('https://api.paypal.com/v1/billing/plans/P-9YY27964PL714174EMXZ67WI', headers=get_prod_http_headers())
    print(response.status_code)
    print(response.text)
