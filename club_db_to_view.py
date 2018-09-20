import pymysql

def club(info):
    conn = pymysql.connect(
        host="localhost",
        user = "root",
        passwd = "1q2w3e4r",
        db = "ajou",
        charset = "utf8",
        use_unicode=True
    )

    cur = conn.cursor()

    sentence1 = 'date'
    sentence2 = 'info'
    sentence3 = 'ajou.haksa'
    sentence4 = 'idhaksa'

    sentence5 = 'club_univ'
    sentence6 = 'club_name'
    sentence7 = 'club_category'
    sentence8 = 'club_major'
    sentence9 = 'ajou.club'

    # 중앙동아리 전체
    if info == '중앙동아리 전체':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence5 + " like " + "'%" + "중앙동아리" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + '\n'
            
        
    # 중앙동아리 관심사 별 분류

    elif info == 'MIDI ':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence5 + " like " + "'%" + "중앙동아리" + "%'" + \
                " AND " + sentence7 + " like " + "'%" + "MIDI" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
            
    elif info == '검도 ':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence5 + " like " + "'%" + "중앙동아리" + "%'" + \
                " AND " + sentence7 + " like " + "'%" + "검도" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
            
    elif info == '광고 ':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence5 + " like " + "'%" + "중앙동아리" + "%'" + \
                " AND " + sentence7 + " like " + "'%" + "광고" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
            
    elif info == '권투 ':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence5 + " like " + "'%" + "중앙동아리" + "%'" + \
                " AND " + sentence7 + " like " + "'%" + "권투" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
            
    elif info == '기타 ':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence5 + " like " + "'%" + "중앙동아리" + "%'" + \
                " AND " + sentence7 + " like " + "'%" + "기타" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
            
    elif info == '농구 ':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence5 + " like " + "'%" + "중앙동아리" + "%'" + \
                " AND " + sentence7 + " like " + "'%" + "농구" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
            
    elif info == '등산 ':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence5 + " like " + "'%" + "중앙동아리" + "%'" + \
                " AND " + sentence7 + " like " + "'%" + "등산" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
            
    elif info == '로봇 ':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence5 + " like " + "'%" + "중앙동아리" + "%'" + \
                " AND " + sentence7 + " like " + "'%" + "로봇" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
            
    elif info == '록 ':
            
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence5 + " like " + "'%" + "중앙동아리" + "%'" + \
                " AND " + sentence7 + " like " + "'%" + "록" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
            
    elif info == '미술 ':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence5 + " like " + "'%" + "중앙동아리" + "%'" + \
                " AND " + sentence7 + " like " + "'%" + "미술" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
            
    elif info == '바둑 ':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence5 + " like " + "'%" + "중앙동아리" + "%'" + \
                " AND " + sentence7 + " like " + "'%" + "바둑" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
            
    elif info == '발명 ':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence5 + " like " + "'%" + "중앙동아리" + "%'" + \
                " AND " + sentence7 + " like " + "'%" + "발명" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
            
    elif info == '발표 ':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence5 + " like " + "'%" + "중앙동아리" + "%'" + \
                " AND " + sentence7 + " like " + "'%" + "발표" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
            
    elif info == '배드민턴 ':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence5 + " like " + "'%" + "중앙동아리" + "%'" + \
                " AND " + sentence7 + " like " + "'%" + "배드민턴" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
            
    elif info == '볼링 ':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence5 + " like " + "'%" + "중앙동아리" + "%'" + \
                " AND " + sentence7 + " like " + "'%" + "볼링" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    elif info == '봉사 ':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence5 + " like " + "'%" + "중앙동아리" + "%'" + \
                " AND " + sentence7 + " like " + "'%" + "봉사" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    elif info == '사진 ':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence5 + " like " + "'%" + "중앙동아리" + "%'" + \
                " AND " + sentence7 + " like " + "'%" + "사진" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    elif info == '서예 ':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence5 + " like " + "'%" + "중앙동아리" + "%'" + \
                " AND " + sentence7 + " like " + "'%" + "서예" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    elif info == '스노우보드 ':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence5 + " like " + "'%" + "중앙동아리" + "%'" + \
                " AND " + sentence7 + " like " + "'%" + "스노우보드" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    elif info == '스쿼시 ':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence5 + " like " + "'%" + "중앙동아리" + "%'" + \
                " AND " + sentence7 + " like " + "'%" + "스쿼시" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    elif info == '시사 ':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence5 + " like " + "'%" + "중앙동아리" + "%'" + \
                " AND " + sentence7 + " like " + "'%" + "시사" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    elif info == '실용음악 ':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence5 + " like " + "'%" + "중앙동아리" + "%'" + \
                " AND " + sentence7 + " like " + "'%" + "실용음악" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    elif info == '야구 ':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence5 + " like " + "'%" + "중앙동아리" + "%'" + \
                " AND " + sentence7 + " like " + "'%" + "야구" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    elif info == '야학 ':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence5 + " like " + "'%" + "중앙동아리" + "%'" + \
                " AND " + sentence7 + " like " + "'%" + "야학" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    elif info == '연극 ':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence5 + " like " + "'%" + "중앙동아리" + "%'" + \
                " AND " + sentence7 + " like " + "'%" + "연극" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    elif info == '영상 ':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence5 + " like " + "'%" + "중앙동아리" + "%'" + \
                " AND " + sentence7 + " like " + "'%" + "영상" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    elif info == '영어 ':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence5 + " like " + "'%" + "중앙동아리" + "%'" + \
                " AND " + sentence7 + " like " + "'%" + "영어" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    elif info == '영화 ':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence5 + " like " + "'%" + "중앙동아리" + "%'" + \
                " AND " + sentence7 + " like " + "'%" + "영화" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    elif info == '유도 ':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence5 + " like " + "'%" + "중앙동아리" + "%'" + \
                " AND " + sentence7 + " like " + "'%" + "유도" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    elif info == '음악 ':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence5 + " like " + "'%" + "중앙동아리" + "%'" + \
                " AND " + sentence7 + " like " + "'%" + "음악" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    elif info == '자전거 ':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence5 + " like " + "'%" + "중앙동아리" + "%'" + \
                " AND " + sentence7 + " like " + "'%" + "자전거" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    elif info == '종교 ':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence5 + " like " + "'%" + "중앙동아리" + "%'" + \
                " AND " + sentence7 + " like " + "'%" + "종교" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    elif info == '천문 ':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence5 + " like " + "'%" + "중앙동아리" + "%'" + \
                " AND " + sentence7 + " like " + "'%" + "천문" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    elif info == '축구 ':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence5 + " like " + "'%" + "중앙동아리" + "%'" + \
                " AND " + sentence7 + " like " + "'%" + "축구" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    elif info == '컴퓨터 ':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence5 + " like " + "'%" + "중앙동아리" + "%'" + \
                " AND " + sentence7 + " like " + "'%" + "컴퓨터" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    elif info == '탁구 ':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence5 + " like " + "'%" + "중앙동아리" + "%'" + \
                " AND " + sentence7 + " like " + "'%" + "탁구" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    elif info == '태권도 ':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence5 + " like " + "'%" + "중앙동아리" + "%'" + \
                " AND " + sentence7 + " like " + "'%" + "태권도" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    elif info == '테니스 ':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence5 + " like " + "'%" + "중앙동아리" + "%'" + \
                " AND " + sentence7 + " like " + "'%" + "테니스" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    elif info == '패러글라이딩 ':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence5 + " like " + "'%" + "중앙동아리" + "%'" + \
                " AND " + sentence7 + " like " + "'%" + "패러글라이딩" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    elif info == '풍물 ':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence5 + " like " + "'%" + "중앙동아리" + "%'" + \
                " AND " + sentence7 + " like " + "'%" + "풍물" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    elif info == '합창 ':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence5 + " like " + "'%" + "중앙동아리" + "%'" + \
                " AND " + sentence7 + " like " + "'%" + "합창" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    elif info == '흑인음악 ':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence5 + " like " + "'%" + "중앙동아리" + "%'" + \
                " AND " + sentence7 + " like " + "'%" + "흑인음악" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    elif info == '힙합 ':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence5 + " like " + "'%" + "중앙동아리" + "%'" + \
                " AND " + sentence7 + " like " + "'%" + "힙합" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        

    # 소학회
    elif info == '소학회':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence7 + " like " + "'%" + "소학회" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    # 각 학과별 검색
    elif info == 'e-비즈니스 학과':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence8 + " like " + "'%" + "e-비즈니스 학과" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    elif info == '건설시스템공학과':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence8 + " like " + "'%" + "건설시스템공학과" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    elif info == '건축학과':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence8 + " like " + "'%" + "건축학과" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    elif info == '경영학과':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence8 + " like " + "'%" + "경영학과" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    elif info == '경제학과':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence8 + " like " + "'%" + "경제학과" + "%'"

        cur.execute(querys)
        total = cur.fetchall()
        result = '※ ' + info + '\n'
        result += '  소속 대학 ' + ' | ' + '   동아리명   ' + ' | ' + ' 분류  ' + ' | ' + '   소속 학과   ' + '\n'
        for row in range(0,len(total)):
            result += total[row][0] + '\n'
            
    elif info == '교통시스템공학과':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence8 + " like " + "'%" + "교통시스템공학과" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    elif info == '국어국문학과':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence8 + " like " + "'%" + "국어국문학과" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    elif info == '금융공학과':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence8 + " like " + "'%" + "금융공학과" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
            
        
    elif info == '기계공학과':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence8 + " like " + "'%" + "기계공학과" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    elif info == '문화컨텐츠학과':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence8 + " like " + "'%" + "문화컨텐츠학과" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    elif info == '물리학과':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence8 + " like " + "'%" + "물리학과" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    elif info == '미디어학과':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence8 + " like " + "'%" + "미디어학과" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    elif info == '불어불문학과':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence8 + " like " + "'%" + "불어불문학과" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    elif info == '사이버보안학과':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence8 + " like " + "'%" + "사이버보안학과" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    elif info == '사학과':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence8 + " like " + "'%" + "사학과" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    elif info == '사회학과':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence8 + " like " + "'%" + "사회학과" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    elif info == '산업공학과':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence8 + " like " + "'%" + "산업공학과" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    elif info == '생명과학과':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence8 + " like " + "'%" + "생명과학과" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    elif info == '소프트웨어학과':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence8 + " like " + "'%" + "소프트웨어학과" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    elif info == '수학과':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence8 + " like " + "'%" + "수학과" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    elif info == '스포츠레저학과':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence8 + " like " + "'%" + "스포츠레저학과" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    elif info == '신소재공학과':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence8 + " like " + "'%" + "신소재공학과" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    elif info == '심리학과':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence8 + " like " + "'%" + "심리학과" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    elif info == '영어영문학과':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence8 + " like " + "'%" + "영어영문학과" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    elif info == '응용화학생명공학과':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence8 + " like " + "'%" + "응용화학생명공학과" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    elif info == '전자공학과':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence8 + " like " + "'%" + "전자공학과" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    elif info == '정치외교학과':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence8 + " like " + "'%" + "정치외교학과" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    elif info == '행정학과':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence8 + " like " + "'%" + "행정학과" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    elif info == '화학공학과':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence8 + " like " + "'%" + "화학공학과" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    elif info == '화학과':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence8 + " like " + "'%" + "화학과" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    elif info == '환경안전공학과':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence8 + " like " + "'%" + "환경안전공학과" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    # 각 대학별 분류

    elif info == '간호대학':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence5 + " like " + "'%" + "간호대학" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
                
    elif info == '경영대학':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence5 + " like " + "'%" + "경영대학" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    elif info == '공과대학':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence5 + " like " + "'%" + "공과대학" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    elif info == '국제학부':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence5 + " like " + "'%" + "국제학부" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    elif info == '사회과학대학':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence5 + " like " + "'%" + "사회과학대학" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    elif info == '약학대학':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence5 + " like " + "'%" + "약학대학" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    elif info == '의과대학':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence5 + " like " + "'%" + "의과대학" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    elif info == '인문대학':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence5 + " like " + "'%" + "인문대학" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    elif info == '자연과학대학':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence5 + " like " + "'%" + "자연과학대학" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    elif info == '정보통신대학':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence5 + " like " + "'%" + "정보통신대학" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    # 각 동아리 관심사 별 분류

    elif info == 'MIDI':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence7 + " like " + "'%" + "MIDI" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    elif info == '검도':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence7 + " like " + "'%" + "검도" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    elif info == '게임개발':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence7 + " like " + "'%" + "게임개발" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    elif info == '경제':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence7 + " like " + "'%" + "경제" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    elif info == '공연':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence7 + " like " + "'%" + "공연" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    elif info == '광고':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence7 + " like " + "'%" + "광고" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    elif info == '권투':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence7 + " like " + "'%" + "권투" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    elif info == '기타':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence7 + " like " + "'%" + "기타" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    elif info == '농구':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence7 + " like " + "'%" + "농구" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    elif info == '독서토론':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence7 + " like " + "'%" + "독서토론" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    elif info == '등산':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence7 + " like " + "'%" + "등산" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    elif info == '로봇':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence7 + " like " + "'%" + "로봇" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    elif info == '록':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence7 + " like " + "'%" + "록" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    elif info == '만화':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence7 + " like " + "'%" + "만화" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    elif info == '문예창작':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence7 + " like " + "'%" + "문예창작" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
                
    elif info == '미술':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence7 + " like " + "'%" + "미술" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    elif info == '바둑':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence7 + " like " + "'%" + "바둑" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    elif info == '발명':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence7 + " like " + "'%" + "발명" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    elif info == '발표':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence7 + " like " + "'%" + "발표" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    elif info == '배드민턴':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence7 + " like " + "'%" + "배드민턴" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    elif info == '볼링':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence7 + " like " + "'%" + "볼링" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    elif info == '봉사':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence7 + " like " + "'%" + "봉사" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    elif info == '분자생물학':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence7 + " like " + "'%" + "분자생물학" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    elif info == '사물놀이':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence7 + " like " + "'%" + "사물놀이" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    elif info == '사진':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence7 + " like " + "'%" + "사진" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    elif info == '사회과학':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence7 + " like " + "'%" + "사회과학" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    elif info == '서예':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence7 + " like " + "'%" + "서예" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    elif info == '수화':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence7 + " like " + "'%" + "수화" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    elif info == '스노우보드':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence7 + " like " + "'%" + "스노우보드" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    elif info == '스쿼시':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence7 + " like " + "'%" + "스쿼시" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    elif info == '시사':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence7 + " like " + "'%" + "시사" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    elif info == '실용음악':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence7 + " like " + "'%" + "실용음악" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    elif info == '야구':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence7 + " like " + "'%" + "야구" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    elif info == '야학':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence7 + " like " + "'%" + "야학" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    elif info == '연극':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence7 + " like " + "'%" + "연극" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    elif info == '영상':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence7 + " like " + "'%" + "영상" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
        
    elif info == '영어':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence7 + " like " + "'%" + "영어" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
                
    elif info == '영화':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence7 + " like " + "'%" + "영화" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
                
    elif info == '오케스트라':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence7 + " like " + "'%" + "오케스트라" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
            
        
    elif info == '유도':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence7 + " like " + "'%" + "유도" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
                
    elif info == '음악':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence7 + " like " + "'%" + "음악" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
                
    elif info == '임용고시':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence7 + " like " + "'%" + "임용고시" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
                
    elif info == '자전거':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence7 + " like " + "'%" + "자전거" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
                
    elif info == '종교':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence7 + " like " + "'%" + "종교" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
                
    elif info == '창업':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence7 + " like " + "'%" + "창업" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
                
    elif info == '천문':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence7 + " like " + "'%" + "천문" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
                
    elif info == '체육':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence7 + " like " + "'%" + "체육" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
                
    elif info == '축구':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence7 + " like " + "'%" + "축구" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
                
    elif info == '춤':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence7 + " like " + "'%" + "춤" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
                
    elif info == '컴퓨터':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence7 + " like " + "'%" + "컴퓨터" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
                
    elif info == '탁구':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence7 + " like " + "'%" + "탁구" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
                
    elif info == '태권도':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence7 + " like " + "'%" + "태권도" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
                
    elif info == '테니스':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence7 + " like " + "'%" + "테니스" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
                
    elif info == '토론':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence7 + " like " + "'%" + "토론" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
                
    elif info == '패러글라이딩':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence7 + " like " + "'%" + "패러글라이딩" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
        
    elif info == '풍물':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence7 + " like " + "'%" + "풍물" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
                
    elif info == '합창':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence7 + " like " + "'%" + "합창" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
                
    elif info == '흑인음악':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence7 + " like " + "'%" + "흑인음악" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
            
                
    elif info == '힙합':
            querys = \
                "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
                " FROM " + sentence9 + \
                " WHERE " + sentence7 + " like " + "'%" + "힙합" + "%'"

            cur.execute(querys)
            total = cur.fetchall()
            result = '※   ' + info + '  ※' + '\n'
            result += '  소속 대학 ' + ' | ' + '동아리명' + ' | ' + '분류' + ' | ' + '소속 학과' + '\n'
            for row in range(0,len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'

    else :
        querys = \
            "SELECT " + sentence1 + ", " + sentence2 + \
            " from " + sentence3 + \
            " where " + sentence2 + " LIKE " + "'%" + info + "%'"
        
        cur.execute(querys)
        total = cur.fetchall()
        result = '※   ' + info + '  ※' + '\n'
        if len(total) > 0 :
            for row in range(0, len(total)):
                result += total[row][0] + ' | ' + total[row][1] + ' | '  + total[row][2] + ' | '  + total[row][3] + '\n'
        else :
            result = '동아리엔 해당 검색 결과가 없어요ㅜㅜ'

    conn.close()

    return result


