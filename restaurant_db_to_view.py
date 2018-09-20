import pymysql
from datetime import datetime

t = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday','saturday','sunday']
r = ['월', '화', '수', '목', '금','토','일']
today = datetime.today().weekday()

def push_count(keyword):

    conn = pymysql.connect(
        host="localhost",
        user = "root",
        passwd = "1q2w3e4r",
        db = "ajou",
        charset = "utf8",
        use_unicode=True
    )

    cur = conn.cursor()

    sql = "UPDATE ajou.restaurant_keyword_list SET " + t[today] + " = " + t[today] + "+ 1" + " WHERE category = '"+keyword+"'" 
    cur.execute(sql)
    conn.commit()
    conn.close()

def pull_rate(day):
    
    conn = pymysql.connect(
        host="localhost",
        user = "root",
        passwd = "1q2w3e4r",
        db = "ajou",
        charset = "utf8",
        use_unicode=True
    )

    cur = conn.cursor()
    sql = \
    "select ((select sum(" + day + ") from restaurant_keyword_list where category = '한식') /" \
	"(select sum(" + day + ") from restaurant_keyword_list) *100)as korea," \
    \
    "((select sum(" + day + ") from restaurant_keyword_list where category = '일식') /" \
	"(select sum(" + day + ") from restaurant_keyword_list) *100)as japan,"\
    \
    "((select sum(" + day + ") from restaurant_keyword_list where category = '중식') /" \
	"(select sum(" + day + ") from restaurant_keyword_list) *100)as china," \
	\
    "((select sum(" + day + ") from restaurant_keyword_list where category = '치킨') /" \
    "(select sum(" + day + ") from restaurant_keyword_list) *100)as chinken," \
    \
    "((select sum(" + day + ") from restaurant_keyword_list where category = '피자') /" \
	"(select sum(" + day + ") from restaurant_keyword_list) *100)as pizza," \
    \
    "((select sum(" + day + ") from restaurant_keyword_list where category = '햄버거') /" \
	"(select sum(" + day + ") from restaurant_keyword_list) *100)as hamburger from restaurant_keyword_list limit 1"
    
    cur.execute(sql)
    rate = cur.fetchall()
    conn.close()

    result = '**' + r[today] + '요일 배달음식 검색통계** \n\n'

    for row in range(0,len(rate)):
	    result += '한식' + ' ☞  ' + str(rate[row][0]) + '(%)\n' +\
	    '일식' + ' ☞  ' + str(rate[row][1]) + '(%)\n' + \
	    '중식' + ' ☞  ' + str(rate[row][2]) + '(%)\n' + \
	    '치킨' + ' ☞  ' + str(rate[row][3]) + '(%)\n' + \
	    '피자' + ' ☞  ' + str(rate[row][4]) + '(%)\n' + \
	    '햄버거' + ' ☞  ' + str(rate[row][5]) + '(%)\n'
    return result

def pull_info(keyword):
    
    conn = pymysql.connect(
        host="localhost",
        user = "root",
        passwd = "1q2w3e4r",
        db = "ajou",
        charset = "utf8",
        use_unicode=True
    )


    cur = conn.cursor()
    sql = "select location, phone_number from restaurant where restaurant = '"+keyword+"'"

    cur.execute(sql)
    total = cur.fetchall()
    conn.close()

    result = '**' + keyword + ' 배달 정보!** \n\n'

    for row in range(0,len(total)):
	    result += '홈페이지 URL' + ' ☞  ' + str(total[row][0]) + '\n' +\
	    '전화번호' + ' ☞  ' + str(total[row][1]) + '\n'
    return result