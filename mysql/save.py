import pymysql
from pymysql.converters import escape_string

def lenCheck(info):
    st1 = len(info[0]) <= 30
    st2 = len(info[1]) <= 300
    st3 = len(info[2]) <= 500
    st4 = len(info[3]) <= 1000
    return st1 and st2 and st3 and st4

def s(l):
    db = pymysql.connect(host='localhost', port=3306, user='root',
                        passwd='sql123', database='webs', charset='utf8')
                        
    cursor = db.cursor()

    try:
        for i in range(len(l)):
            info = l[i]
            inf1 = escape_string(info[0])
            inf2 = escape_string(info[1])
            inf3 = escape_string(info[2])
            inf4 = escape_string(info[3])
            sql = "insert into web(ip, title, keywords, description)" \
            "values('%s', '%s',  '%s', '%s')"%(inf1, inf2, inf3, inf4)
            if lenCheck(info): cursor.execute(sql)
    finally:
        db.commit()
        cursor.close()
        db.close()
