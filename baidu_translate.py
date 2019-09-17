#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
import requests
import execjs


class BaiduTranslateJS(object):

    def __init__(self, keyword=None):
        self.url = 'https://fanyi.baidu.com/v2transapi'
        self.keyword = keyword
        self.data = {
            'from': 'en',
            'to': 'zh',
            'query': self.keyword,
            'transtype': 'translang',
            'simple_means_flag': '3',
            'sign': '',
            'token': '187ddb473d5526c5cce3241a389d80e4',
        }
        self.headers = {
            'cookie': 'BAIDUID=B30423C966FF8D3E58FBB7A66552A2EE:FG=1; BIDUPSID=B30423C966FF8D3E58FBB7A66552A2EE; PSTM=1564016819; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; MCITY=-%3A; APPGUIDE_8_0_0=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; __cfduid=dbb201cfbd23cff106d83bdfdbe8329bd1568605107; H_PS_PSSID=29634_1422_21086_29522_29519_29721_29568_29221; BDUSS=zZZWmRabDB2VTU5TUlzZnVlY3dDdUNaa1BoaWtod2ZWa2JycXZRQlhJaEMwNmRkSUFBQUFBJCQAAAAAAAAAAAEAAAAsLQLCv9Ww125pY2UwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEJGgF1CRoBda; BDSFRCVID=ZrFOJeCmH6VwoRJwA3ojrUSPJeKK0gOTHllvouZ9B1IsoBkVJeC6EG0Ptf8g0KubFTPRogKK0gOTH6KF_2uxOjjg8UtVJeC6EG0P3J; H_BDCLCKID_SF=tJkD_I_hJKt3qn7I5KToh4Athxob2bbXHDo-LIvgaqvcOR5JhfA-3R-e046f36ON5jrPbMJF5lvvhb3O3M7Shb5Djh-8Qf30BDOQaMQF5l8-sq0x0bOte-bQypoa0q3TLDOMahkM5h7xOKQoQlPK5JkgMx6MqpQJQeQ-5KQN3KJmhpFuD6taj5jLjN0sb-RhbPoyWJRVaJ5fDP3kq4Tq55PlK4j9BtQmam-q-t3OLqcbEDOvMR5l0p8pbtRiJPb9QgbQWPQObxFBECjVKPnIMpKpbt-q0x-jLTnhVn0MW-5DsxbM04nJyUnQbPnnBT5i3H8HL4nv2JcJbM5m3x6qLTKkQN3TJMIEK5r2SCDhtDPW3H; from_lang_often=%5B%7B%22value%22%3A%22kor%22%2C%22text%22%3A%22%u97E9%u8BED%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; delPer=0; PSINO=5; ZD_ENTRY=baidu; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; locale=zh; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1567741513,1568105153,1568711337,1568712790; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1568712790; __yjsv5_shitong=1.0_7_5c7f442d90a4e761415ecf3ce9c15a1d33d8_300_1568712790130_218.82.139.34_77f57434; yjs_js_security_passport=c7905012579476fb8f38c892562b3d38c2743348_1568712790_js; to_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
        }
        self.ctx = None

    def get_sign(self):
        """
        执行js 获取sign
        """
        if self.ctx is None:  # 复用ctx 如果ctx为空才创建
            with open('./baidu_translate_js.js', 'r', encoding='utf-8') as f:
                self.ctx = execjs.compile(f.read())
        sign = self.ctx.call('e', self.keyword)
        self.data['sign'] = sign  # data中的sign参数重新赋值

    def get_response(self):
        self.get_sign()
        response = requests.post(self.url, headers=self.headers, data=self.data)
        # print(response)
        print('翻译结果: ', response.json()['trans_result']['data'][0]['dst'])


if __name__ == '__main__':
    baidu_translate = BaiduTranslateJS('this is a test spider')
    baidu_translate.get_response()
    BaiduTranslateJS('hello world').get_response()
    BaiduTranslateJS('goods').get_response()
