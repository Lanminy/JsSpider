#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
import re
import requests
from lxml import etree
import urllib3
urllib3.disable_warnings()
'''
                         抖音用户基本信息 -> 请求share来获取数据 
'''

def handle_decode(input_data):
    # 匹配icon font
    regex_list = [
        {'name': [' &#xe603; ', ' &#xe60d; ', ' &#xe616; '], 'value': 0},
        {'name': [' &#xe602; ', ' &#xe60e; ', ' &#xe618; '], 'value': 1},
        {'name': [' &#xe605; ', ' &#xe610; ', ' &#xe617; '], 'value': 2},
        {'name': [' &#xe604; ', ' &#xe611; ', ' &#xe61a; '], 'value': 3},
        {'name': [' &#xe606; ', ' &#xe60c; ', ' &#xe619; '], 'value': 4},
        {'name': [' &#xe607; ', ' &#xe60f; ', ' &#xe61b; '], 'value': 5},
        {'name': [' &#xe608; ', ' &#xe612; ', ' &#xe61f; '], 'value': 6},
        {'name': [' &#xe60a; ', ' &#xe613; ', ' &#xe61c; '], 'value': 7},
        {'name': [' &#xe60b; ', ' &#xe614; ', ' &#xe61d; '], 'value': 8},
        {'name': [' &#xe609; ', ' &#xe615; ', ' &#xe61e; '], 'value': 9},
    ]
        #
    for i1 in regex_list:
        for i2 in i1['name']:
            input_data = re.sub(i2, str(i1['value']), input_data)       # 把正确value替换到自定义字体上

    html = etree.HTML(input_data)
    douyin_info = {}

    # 获取昵称
    douyin_info['nick_name'] = html.xpath("//div[@class='personal-card']/div[@class='info1']//p[@class='nickname']/text()")[0]
    # 获取抖音ID
    douyin_id = ''.join(html.xpath("//div[@class='personal-card']/div[@class='info1']/p[@class='shortid']/text()"))
    douyin_id = douyin_id.replace('抖音ID：', '').replace(' ', '')
    i_id = ''.join(html.xpath("//div[@class='personal-card']/div[@class='info1']/p[@class='shortid']/i/text()"))
    douyin_info['douyin_id'] = str(douyin_id) + str(i_id)
    # douyin_info['douyin_id'] = re.sub(search_douyin_str, '', html.xpath("//div[@class='personal-card']/div[@class='info1']//p[@class='nickname']/text()")[0]).strip() + douyin_id
    # 职位类型
    try:
        douyin_info['job'] = html.xpath("//div[@class='personal-card']/div[@class='info2']/div[@class='verify-info']/span[@class='info']/text()")[0].strip()
    except:
        pass
    # 描述
    douyin_info['describe'] = html.xpath("//div[@class='personal-card']/div[@class='info2']/p[@class='signature']/text()")[0].replace('\n', ',')
    # 关注
    douyin_info['follow_count'] = ''.join(html.xpath("//div[@class='personal-card']/div[@class='info2']/p[@class='follow-info']//span[@class='focus block']//i/text()"))
    # 粉丝
    fans_value = ''.join(html.xpath("//div[@class='personal-card']/div[@class='info2']/p[@class='follow-info']//span[@class='follower block']//i[@class='icon iconfont follow-num']/text()"))
    unit = html.xpath("//div[@class='personal-card']/div[@class='info2']/p[@class='follow-info']//span[@class='follower block']/span[@class='num']/text()")
    if unit[-1].strip() == 'w':
        douyin_info['fans'] = str(float(fans_value) / 10) + 'w'
        fans_count = douyin_info['fans'][:-1]
        fans_count = float(fans_count)
        fans_count = fans_count * 10000
        douyin_info['fans_count'] = fans_count
    else:
        douyin_info['fans'] = fans_value
        douyin_info['fans_count'] = fans_value
    # 点赞
    like = ''.join(html.xpath("//div[@class='personal-card']/div[@class='info2']/p[@class='follow-info']//span[@class='liked-num block']//i[@class='icon iconfont follow-num']/text()"))
    unit = html.xpath("//div[@class='personal-card']/div[@class='info2']/p[@class='follow-info']//span[@class='liked-num block']/span[@class='num']/text()")
    if unit[-1].strip() == 'w':
        douyin_info['like'] = str(float(like) / 10) + 'w'
        like_count = douyin_info['like'][:-1]
        like_count = float(like_count)
        like_count = like_count * 10000
        douyin_info['like_count'] = like_count
    else:
        douyin_info['like'] = like
        douyin_info['like_count'] = like

    # 作品
    worko_count = ''.join(html.xpath("//div[@class='video-tab']/div/div[1]//i/text()"))
    douyin_info['work_count'] = worko_count

    return douyin_info


def handle_douyin_info(url):
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'
    }
    response = requests.get(url=url, headers=header, verify=False)
    print(response, url)
    return handle_decode(response.text)

if __name__ == '__main__':
    url = 'https://www.iesdouyin.com/share/user/88445518961'
    print(handle_douyin_info(url))