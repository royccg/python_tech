# -*- coding: utf-8 -*-
# @Author: royccg
# @Date:   2020-06-13 14:47:31
# @Last Modified by:   roy
# @Last Modified time: 2020-06-13 16:15:10
# @Email : roy778555479@gmail.com

import requests


proxies = {'http': 'http://localhost:2334',
           'https': 'http://localhost:2334'}

# url = 'http://www.youtube.com'
url = 'http://www.baidu.com'
proxies = {'http': None, 'https': None}
r = requests.get(url, proxies=proxies, verify=False)
r.encoding = 'utf-8'
print(r.status_code)
print(r.text)
