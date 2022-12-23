import xlrd
import mysql.save

filename = './ips/ip202212231438.xls'
def getInfoFromXls():
    infos = []
    wb = xlrd.open_workbook(filename)
    sheet = wb.sheet_by_index(0)

    print(sheet.ncols)
    print(sheet.nrows)
    for i in range(1, sheet.nrows):
        info = []
        for j in range(sheet.ncols):
            sstr = sheet.cell_value(i, j) or ''
            info.append(sstr)
        infos.append(info)
    return infos

mysql.save.s(getInfoFromXls())