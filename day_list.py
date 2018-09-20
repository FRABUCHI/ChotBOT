import pymysql
from datetime import datetime

#반환값 없음.
def push(keyword):
    
    conn = pymysql.connect(
        host="localhost",
        user = "root",
        passwd = "1q2w3e4r",
        db = "ajou",
        charset = "utf8",
        use_unicode=True
    )

    cur = conn.cursor()

    #중복 되면 카운트 올리고 중복 아닌 키워드는 삽입하고 카운트 올림
    sql = "INSERT INTO ajou.day_keyword_list(keyword) VALUES ('"+keyword+"')" + 'on duplicate key update num = num + 1'
    cur.execute(sql)
    
    conn.commit()
    conn.close()


def pull():
    
    conn = pymysql.connect(
        host="localhost",
        user = "root",
        passwd = "1q2w3e4r",
        db = "ajou",
        charset = "utf8",
        use_unicode=True
    )

    cur = conn.cursor()

    #상위 10개 키워드 가져옴.
    sql = 'select keyword from day_keyword_list order by num desc limit 10'
    cur.execute(sql)
    total = cur.fetchall()
    conn.close()
    
    result = '**오늘의 인기 검색어!** \n\n'
    num = 1
    for row in range(0,len(total)):
        result += str(num) + ' ☞  ' + total[row][0] + '\n'
        num +=1
    
    return result

def init() :
    conn = pymysql.connect(
        host="localhost",
        user = "root",
        passwd = "1q2w3e4r",
        db = "ajou",
        charset = "utf8",
        use_unicode=True
    )
    nowHour = datetime.today().hour
    nowMin = datetime.today().minute
    nowSec = datetime.today().second

    cur = conn.cursor()
    if nowHour == 0 and nowMin == 0 and nowSec == 0:
        sql = 'SET SQL_SAFE_UPDATES =0'
        cur.execute(sql)
        sql = 'UPDATE day_keyword_list SET num = default'
        cur.execute(sql)
        conn.commit()

    conn.close()

init()