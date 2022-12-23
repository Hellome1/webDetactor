import random
sequence = 'abcdefghijklmnopqrstuvwxyz0123456789'

def joinIp(ip):
    return 'http://www.' + ip + '.com'

def getRandomIp():
    num = random.randint(3, 7)
    ip = ''.join(random.sample(sequence, num))
    return joinIp(ip)

def getAllIp(num):
    seq = []
    maxL = len(sequence)
    while len(seq) < num:
        seq.append(0)
    def addOne():
        i = len(seq) - 1
        while i >= 0:
            if (i == len(seq) - 1): seq[i] += 1
            if seq[i] == maxL:
                if i - 1 >= 0:
                    seq[i] = 0
                    seq[i - 1] += 1
            i -= 1

    def a():
        ip  =''
        for i in range(len(seq)):
            ip += sequence[seq[i]]
        addOne()
        print(ip)
        return ip

    def logseq():
        print(seq)

    return {
        'get': a,
        'log': logseq
    }

ins = getAllIp(3)
num = 37
while num >= 0:
    ins['get']()
    ins['log']()
    num -= 1