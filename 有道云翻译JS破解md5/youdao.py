#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import time
import random
import hashlib

url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
    'Cookie': 'OUTFOX_SEARCH_USER_ID_NCOO=570464452.7723297; OUTFOX_SEARCH_USER_ID="-253409441@10.169.0.82"; _ga=GA1.2.1983385948.1564020820; _ntes_nnid=26f5556b6069d13c9858684be300a993,1565337391500; _gid=GA1.2.1290882915.1570508588; JSESSIONID=aaaZJPzGR5nWm_5WiHV2w; ___rl__test__cookies=1570691724762',
    'Host': 'fanyi.youdao.com',
    'Origin': 'http://fanyi.youdao.com',
    'Referer': 'http://fanyi.youdao.com/',
    'X-Requested-With': 'XMLHttpRequest'
}


def fanyi(word):
    ctime = int(round(time.time() * 1000))

    salt = str(ctime + random.randint(1, 10))

    sign = hashlib.md5(('fanyideskweb' + word + salt + 'n%A-rKaT5fb[Gy?;N5@Tj').encode('utf-8')).hexdigest()  # md5
    # print(sign)
    data = {
        'i': word,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': salt,
        'sign': sign,
        'ts': ctime,  # 毫秒级时间戳
        'bv': 'ca3dedaa9d15daa003db daaa991540d1',  # 不变
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTlME'
    }

    resp = requests.post(url=url, data=data, headers=headers)
    print(resp.json())


if __name__ == '__main__':
    fanyi('hello')
