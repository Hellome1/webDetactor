def notOne(l, i):
    if i != 0:
        return 1
    return 0

def filter(l):
    nl = []
    cb = notOne
    for i  in range(len(l)):
        if cb(l[i], i): nl.append(l[i])
    return nl