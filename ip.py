import random
sequence = 'abcdefghijklmnopqrstuvwxyz0123456789'
def getRandomIp():
    num = random.randint(3, 7)
    ip = ''.join(random.sample(sequence, num))
    return 'http://www.' + ip + '.com'