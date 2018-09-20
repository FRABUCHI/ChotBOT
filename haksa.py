# -*- coding: utf-8 -*-

import pymysql
import requests
from bs4 import BeautifulSoup

conn = pymysql.connect(
	host="localhost",
	user = "root",
	passwd = "1q2w3e4r",
        db = "ajou",
        charset = "utf8",
        use_unicode=True
)
cur = conn.cursor()

url = "http://www.ajou.ac.kr/new/life/schedule_haksa.jsp"
html = requests.get(url).text

soup = BeautifulSoup(html, "html.parser")
crol = soup.select('td[class=left_pd]')

i=0

for content in crol:
	check = i % 2
	if check == 0 :
		data = content.text
	else :
		data1 = content.text
		sql = "INSERT INTO haksa1(date, info) VALUES ('"+data+"','"+data1+"')"
		cur.execute(sql)
	i += 1

conn.commit()

conn.close()
    

        
