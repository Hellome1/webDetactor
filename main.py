import req
import excelt
import time
import asyncReq

needIpNum = 10
onceReqNum = 2 #一次请求ip数量

header = ['ip', 'title', 'keywords', 'description']
infos = [header] #存储可用的ip以及信息

#请求随机的ip地址直到达到指定数量
def multiReq():
    # for i in range(0, onceReqNum):
    info = req.getIp()
    print(info)
    infos.append(info)

starttime = time.time()
while(len(infos) <= needIpNum):
    print('runing')
    multiReq()

#最后保存
excelt.save(infos)
endtime = time.time()
print('总用时%fs'%(endtime - starttime))