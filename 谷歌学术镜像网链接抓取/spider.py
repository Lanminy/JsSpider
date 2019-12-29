import requests
from lxml import etree
import re
import execjs


with open('scmor.js', 'r', encoding='utf-8') as f:
    js = f.read()
    ctx = execjs.compile(js)
    #编译保存的js

def get_html():
    #请求html
    try:
        r = requests.get("http://ac.scmor.com/")
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print('产生异常')

def parse_html(html):
    #解析html，并用re匹配密文
    tree = etree.HTML(html)
    script_text = tree.xpath('//script/text()')[0]
    autourls = re.findall(r'AD0mWAw[a-zA-Z0-9]+=*', script_text)
    return autourls

def decode(string):
    #利用保存的js解密密文
    return ctx.call('strdecode', string)


if __name__ == '__main__':
    html = get_html()
    autourls = parse_html(html)
    for url in autourls:
        print(decode(url))
    #print(decode('AD0mWAw2VVYgWiAdDB4LHQwqaxY2XxcVL0M9FiEYTxM='))  #decode将源码中的加密字符串转url
