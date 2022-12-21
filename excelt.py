import xlwt
import time

def getTimeStamp():
    t = time.localtime()
    ts = ''
    for i in range(0,5):
        ts += str(t[i])
    return ts

def save(list):
    timestamp = getTimeStamp()
    workbook = xlwt.Workbook(encoding='utf-8')
    sheet = workbook.add_sheet('ips')
    for i in range(0, len(list)):
        row = list[i]
        for j in range(0, len(row)):
            sheet.write(i, j, row[j])
    print(timestamp)
    workbook.save('./ips/ip' + timestamp + '.xls')
