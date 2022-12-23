import asyncio
import requests
from lxml import etree
import time
import aiohttp
import ip
import excelt
import mysql.save
import tool.index

needIpNum = 1000
onceReqNum = 200 #一次请求ip数量

header = ['ip', 'title', 'keywords', 'description']
infos = [header] #存储可用的ip以及信息

async def main(url):
    print(url)

    timeout = aiohttp.ClientTimeout(total=10)
    async with aiohttp.ClientSession(timeout=timeout) as session:
        try:
            async with session.get(url) as response:
                print('res', response.status)
                print("Content-type:", response.headers['content-type'])
                print("{url} 得到响应".format(url=url))
                hl = await response.text()
                html = etree.HTML(hl, parser=etree.HTMLParser(encoding='utf-8'))
                metas = html.xpath('//meta/@name')
                keywords = html.xpath('//meta[@name="keywords"]/@content') and html.xpath('//meta[@name="keywords"]/@content')[0] or ''
                description = html.xpath('//meta[@name="description"]/@content') and html.xpath('//meta[@name="description"]/@content')[0] or ''
                title = html.xpath('//title/text()') and html.xpath('//title/text()')[0] or ''
                # print('__keywords__:', keywords)
                # print('__description__:', description)
                # print('__title__:', title)
                print('__title__:', title[0:5] + '...')
                if keywords or description or title:
                    infos.append([url, title, keywords, description])
        except aiohttp.client_exceptions.ClientConnectorError as e:
            print('eeeeee', e)
        except asyncio.TimeoutError as e:
            print('tttttt', e)
        except:
            print('xxxxxx')
        finally:
            await session.close()

def getlocaltime():
    t = time.localtime()
    return '-'.join([str(t[i]) for i in range(3)]) + ' ' + ':'.join(str(t[i]) for i in range(3, 5))

async def eachUrls():
    tasks = []
    for i in range(onceReqNum):
        task = asyncio.create_task(main(ip.getRandomIp()))
        tasks.append(task)
    start = time.time()
    done, pending = await asyncio.wait(tasks)
    end = time.time()
    print("Complete in {} seconds".format(end - start))
    # for done_task in done:
    #     print((f"[{getlocaltime()}] 得到执行结果 {done_task.result()}"))
            
def start():
    starttime = time.time()
    while len(infos) <= needIpNum:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(eachUrls())
        # time.sleep(1)
        asyncio.sleep(1)
    #最后保存
    excelt.save(infos)
    sqlInfo = tool.index.filter(infos)
    mysql.save.s(sqlInfo)
    endtime = time.time()
    print('总用时%fs'%(endtime - starttime))

start()