import time

def getlocaltime():
    t = time.localtime()
    return '-'.join([str(t[i]) for i in range(3)]) + ' ' + ':'.join(str(t[i]) for i in range(3, 5))

print(getlocaltime())