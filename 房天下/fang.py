#!/usr/bin/env python
# -*- coding: utf-8 -*-
# !/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import execjs

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0; DUK-AL20 Build/HUAWEIDUK-AL20; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/044353 Mobile Safari/537.36 MicroMessenger/6.7.3.1360(0x26070333) NetType/WIFI Language/zh_CN Process/tools',
    'Referer': 'https://passport.fang.com/'
}


class FangJS(object):
    def __init__(self, username=None, password=None):
        self.url = 'https://passport.fang.com/'
        self.login_url = 'https://passport.fang.com/login.api'
        self.username = username
        self.password = password
        self.ctx = None
        self.data = {
            'Service': 'soufun-passport-web',
            'AutoLogin': '1',
            'uid': self.username
        }

    def get_pwd(self):
        """
        执行js 获取pwd
        """
        if self.ctx is None:  # 复用ctx 如果ctx为空才创建
            with open('./fang.js', 'r', encoding='utf-8') as f:
                self.ctx = execjs.compile(f.read())
        print(self.password)
        pwd = self.ctx.call('getPwd', self.password)
        print(pwd)
        self.data['pwd'] = pwd  # data中的pwd参数重新赋值

    def login(self):
        resp = requests.post(self.login_url, headers=HEADERS, data=self.data)
        print(resp.json())


if __name__ == '__main__':
    fang_js = FangJS('房天下账号', '房天下密码')
    fang_js.get_pwd()
    print(fang_js.data)
    fang_js.login()
