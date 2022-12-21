import requests
import chardet
from lxml import etree
import ip
timeoutset = .5
def reqRandomIp():
    try:
        ua = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36' }
        url = ip.getRandomIp()
        print('当前请求：', url)
        r = requests.get(url, timeout=timeoutset)
        r.encoding = chardet.detect(r.content)['encoding']
        hl = r.content.decode('utf-8')
        html = etree.HTML(hl, parser=etree.HTMLParser(encoding='utf-8'))
        metas = html.xpath('//meta/@name')
        keywords = html.xpath('//meta[@name="keywords"]/@content')[0]
        description = html.xpath('//meta[@name="description"]/@content')[0]
        title = html.xpath('//title/text()')[0]
        # print(metas)
        print('__keywords__:', keywords)
        print('__description__:', description)
        print('__title__:', title)
        return [url, title, keywords, description]
    except:
        return ''

def getIp():
    res = ''
    res2 = ''
    while (res == ''):
        res = reqRandomIp()
    return res or res2