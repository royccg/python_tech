# -*- coding: utf-8 -*-
# @Author: royccg
# @Date:   2020-06-13 16:35:39
# @Last Modified by:   roy
# @Last Modified time: 2020-06-13 16:43:03
# @Email : roy778555479@gmail.com

import requests


def getHTMLText(url):
    try:
        proxies = {'http': None, 'https': None}
        r = requests.get(url, timeout=30, proxies=proxies, verify=False)
        r.raise_for_status()  # 如果状态不是200，引发HTTPError异常
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return '产生异常'


if __name__ == '__main__':
    url = 'http://www.baidu.com'
    print(getHTMLText(url))
    # pass
