# import requests
# from parsel import Selector
# wd = input()
# url = f'https://baidu.com/s?wd={wd}'
# res = requests.get(url)
# print(res.status_code)
# print(res.request.url)

import re
import requests
from parsel import Selector



wd = input()
param = {"wd":wd}
url = f'https://baidu.com/s'
res = requests.get(url, params = param)
print(res.status_code)
print(res.request.url)