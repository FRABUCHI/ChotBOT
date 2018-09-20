
#########수정 하지 마세요######################

import pymysql

def haksa_db (info) :

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

    #전체 학사 일정
    if info in ('전체','전체학사일정','학사력'):
        result = '※ ' + info + " 일정표 ※"
        sql = "select date, info from haksa"
        cur.execute(sql)
        date = cur.fetchall()
        for row in range(0, len(date)):
            result += '\n\n' + date[row][0].strip('\n') + '\n' + date[row][1].strip('\n')


    #########################################################################################3
    #1학기 중간/기말/성적  
    elif info == '1학기':
        result = '※ ' + info + " 일정표 ※"
        sql = '''
        SELECT date, info 
        FROM haksa 
        where (info LIKE '%1학기%' and info LIKE '%시험%') or (info LIKE '%1학기%' and info LIKE '%성적%')
        '''
        cur.execute(sql)
        date = cur.fetchall()
        for row in range(0, len(date)):
            result += '\n\n' + date[row][0].strip('\n') + '\n' + date[row][1].strip('\n')
        
    #2학기 중간/기말/성적  
    elif info == '2학기':
        result = '※ ' + info + " 일정표 ※"
        sql = '''
        SELECT date, info 
        FROM haksa 
        where (info LIKE '%2학기%' and info LIKE '%시험%') or (info LIKE '%2학기%' and info LIKE '%성적%')
        '''
        cur.execute(sql)
        date = cur.fetchall()
        for row in range(0, len(date)):
            result += '\n\n' + date[row][0].strip('\n') + '\n' + date[row][1].strip('\n')

    #1학기/2학기 중간/기말/성적
    elif info in ('중간','중간고사','기말','기말고사','성적','성적입력','성적정정','공고'):
        result = '※ ' + info + " 일정표 ※"
        sql = '''
        SELECT date, info 
        FROM haksa 
        where (info LIKE '%1학기%' and info LIKE '%시험%') or (info LIKE '%1학기%' and info LIKE '%성적%') or (info LIKE '%2학기%' and info LIKE '%시험%') or (info LIKE '%2학기%' and info LIKE '%성적%')
        '''
        cur.execute(sql)
        date = cur.fetchall()
        for row in range(0, len(date)):
            result += '\n\n' + date[row][0].strip('\n') + '\n' + date[row][1].strip('\n')
    
    #########################################################################################3
    # 개강
    elif info == '개강':
        result = '※ ' + info + " 일정표 ※"
        querys = \
            "SELECT " + sentence1 + ", " + sentence2 + \
            " FROM " + sentence3 + \
            " WHERE " + sentence2 + " like " + "'%" + "개강" + "%'"

        cur.execute(querys)
        date = cur.fetchall()
        for row in range(0, len(date)):
            result += '\n\n' + date[row][0].strip('\n') + '\n' + date[row][1].strip('\n')

    #########################################################################################3
    # 예비수강
    elif info == '예비수강':
        result = '※ ' + info + " 일정표 ※"
        querys = \
            "SELECT " + sentence1 + ", " + sentence2 + \
            " FROM " + sentence3 + \
            " WHERE " + sentence2 + " like " + "'%" + "책가방식" + "%'"

        cur.execute(querys)
        date = cur.fetchall()
        for row in range(0, len(date)):
            result += '\n\n' + date[row][0].strip('\n') + '\n' + date[row][1].strip('\n')

    # 수강신청
    elif info == '수강신청':
        result = '※ ' + info + " 일정표 ※"
        querys = \
            "SELECT " + sentence1 + ", " + sentence2 + \
            " FROM " + sentence3 + \
            " WHERE " + sentence2 + \
            " like " + "'%" + "수강신청" + "%'" + \
            " and " + " not info like " + "'%" + "포기" + "%'" + \
            " and " + " not info like " + "'%" + "예비" + "%'"

        cur.execute(querys)
        date = cur.fetchall()
        for row in range(0, len(date)):
            result += '\n\n' + date[row][0].strip('\n') + '\n' + date[row][1].strip('\n')

    # 수강정정
    elif info == '수강정정':
        result = '※ ' + info + " 일정표 ※"
        querys = \
            "SELECT " + sentence1 + ", " + sentence2 + \
            " FROM " + sentence3 + \
            " WHERE " + sentence2 + " like " + "'%" + "수강정정" + "%'"

        cur.execute(querys)
        date = cur.fetchall()
        for row in range(0, len(date)):
            result += '\n\n' + date[row][0].strip('\n') + '\n' + date[row][1].strip('\n')

    # 수강신청포기
    elif info == '수강신청 포기':
        result = '※ ' + info + " 일정표 ※"
        querys = \
            "SELECT " + sentence1 + ", " + sentence2 + \
            " FROM " + sentence3 + \
            " WHERE " + sentence2 + " like " + "'%" + "수강신청포기" + "%'"

        cur.execute(querys)
        date = cur.fetchall()
        for row in range(0, len(date)):
            result += '\n\n' + date[row][0].strip('\n') + '\n' + date[row][1].strip('\n')

    # 취득학점포기
    elif info == '취득학점 포기':
        result = '※ ' + info + " 일정표 ※"
        querys = \
            "SELECT " + sentence1 + ", " + sentence2 + \
            " FROM " + sentence3 + \
            " WHERE " + sentence2 + " like " + "'%" + "취득학점포기" + "%'"

        cur.execute(querys)
        date = cur.fetchall()
        for row in range(0, len(date)):
            result += '\n\n' + date[row][0].strip('\n') + '\n' + date[row][1].strip('\n')

########################################################################################################
    #방학관련 일정 
    elif info == '방학':
        result = '※ ' + info + " 일정표 ※"
        querys = \
            "SELECT " + sentence1 + ", " + sentence2 + \
            " from " + sentence3 + \
            " where " + sentence2 + " LIKE " + "'%" + "방학" + "%'"
        cur.execute(querys)
        date = cur.fetchall()
        for row in range(0, len(date)):
            result += '\n\n' + date[row][0].strip('\n') + '\n' + date[row][1].strip('\n')

    #방학관련 일정 
    elif info == '여름방학':
        result = '※ ' + info + " 일정표 ※"
        querys = \
            "SELECT " + sentence1 + ", " + sentence2 + \
            " from " + sentence3 + \
            " where " + sentence2 + " LIKE " + "'%" + "방학" + "%'" + \
            " and " + " not info like " + "'%" + "동계" + "%'"

        cur.execute(querys)
        date = cur.fetchall()
        for row in range(0, len(date)):
            result += '\n\n' + date[row][0].strip('\n') + '\n' + date[row][1].strip('\n')


    #방학관련 일정 
    elif info == '겨울방학':
        result = '※ ' + info + " 일정표 ※"
        querys = \
            "SELECT " + sentence1 + ", " + sentence2 + \
            " from " + sentence3 + \
            " where " + sentence2 + " LIKE " + "'%" + "날" + "%'" + \
            " and " + " not info like " + "'%" + "하계" + "%'"

        cur.execute(querys)
        date = cur.fetchall()
        for row in range(0, len(date)):
            result += '\n\n' + date[row][0].strip('\n') + '\n' + date[row][1].strip('\n')

########################################################################################################
    #휴일관련 일정 
    elif info in ('휴일', '공휴일', '쉬는날'):
        result = '※ ' + info + " 일정표 ※"
        querys = \
            "SELECT " + sentence1 + ", " + sentence2 + \
            " from " + sentence3 + \
            " where " + sentence2 + " LIKE " + "'%" + "날" + "%'" + \
            " UNION ALL " + \
            "SELECT " + sentence1 + ", " + sentence2 + \
            " from " + sentence3 + \
            " where " + sentence2 + " LIKE " + "'%" + "절" + "%'" + \
            " and " + " not info like " + "'%" + "계절" + "%'" + \
            " UNION ALL " + \
            "SELECT " + sentence1 + ", " + sentence2 + \
            " from " + sentence3 + \
            " where " + sentence2 + " LIKE " + "'%" + "일" + "%'" + \
            " and " + " not info like " + "'%" + "수업" + "%'" + \
            " and " + " not info like " + "'%" + "일절" + "%'" + \
            " and " + " not info like " + "'%" + "보강" + "%'" + \
            " and " + " not info like " + "'%" + "학위" + "%'" + \
            " UNION ALL " + \
            "SELECT " + sentence1 + ", " + sentence2 + \
            " from " + sentence3 + \
            " where " + sentence2 + " LIKE " + "'%" + "연휴" + "%'" + \
            " UNION ALL " + \
            "SELECT " + sentence1 + ", " + sentence2 + \
            " from " + sentence3 + \
            " where " + sentence2 + " LIKE " + "'%" + "선거" + "%'"

        cur.execute(querys)
        date = cur.fetchall()
        for row in range(0, len(date)):
            result += '\n\n' + date[row][0].strip('\n') + '\n' + date[row][1].strip('\n')

########################################################################################################
    #행정관련 일정
    elif info in('전과', '전과신청', '전과 신청'):
        result = '※ ' + info + " 일정표 ※"
        querys = \
            "SELECT " + sentence1 + ", " + sentence2 + \
            " from " + sentence3 + \
            " where " + sentence2 + " LIKE " + "'%" + "전과" + "%'"
        cur.execute(querys)
        date = cur.fetchall()
        for row in range(0, len(date)):
            result += '\n\n' + date[row][0].strip('\n') + '\n' + date[row][1].strip('\n')

    #행정관련 일정
    elif info in('학기등록', '등록', '학기 등록'):
        result = '※ ' + info + " 일정표 ※"
        querys = \
            "SELECT " + sentence1 + ", " + sentence2 + \
            " from " + sentence3 + \
            " where " + sentence2 + " LIKE " + "'%" + "등록" + "%'"
        cur.execute(querys)
        date = cur.fetchall()
        for row in range(0, len(date)):
            result += '\n\n' + date[row][0].strip('\n') + '\n' + date[row][1].strip('\n')

    #행정관련 일정
    elif info in('전공/졸업 신청', '졸업유예', '졸업연기', '졸업 유예', '졸업 연기', '전공 변경', '전공 취소', '복수전공', '부전공', '연계전공'):
        result = '※ ' + info + " 일정표 ※"
        querys = \
            "SELECT " + sentence1 + ", " + sentence2 + \
            " from " + sentence3 + \
            " where " + sentence2 + " LIKE " + "'%" + "졸업" + "%'"
        cur.execute(querys)
        date = cur.fetchall()
        for row in range(0, len(date)):
            result += '\n\n' + date[row][0].strip('\n') + '\n' + date[row][1].strip('\n')

########################################################################################################
    #입학/졸업 관련 일정
    elif info in ('입학식','입학식(신·편입)'):
        result = '※ ' + info + " 일정표 ※"
        querys = \
            "SELECT " + sentence1 + ", " + sentence2 + \
            " from " + sentence3 + \
            " where (" + sentence2 + " LIKE '%" + "입학식" + "%') or (" + sentence2 + " LIKE '%" + "오리엔테이션" + "%')"

        cur.execute(querys)
        date = cur.fetchall()
        for row in range(0, len(date)):
            result += '\n\n' + date[row][0].strip('\n') + '\n' + date[row][1].strip('\n')

    #입학/졸업 관련 일정
    elif info in ('졸업식','졸업식(학위 수여식)'):
        result = '※ ' + info + " 일정표 ※"
        querys = \
            "SELECT " + sentence1 + ", " + sentence2 + \
            " from " + sentence3 + \
            " where " + sentence2 + " LIKE " + "'%" + "학위" + "%'"
        
        cur.execute(querys)
        date = cur.fetchall()
        for row in range(0, len(date)):
            result += '\n\n' + date[row][0].strip('\n') + '\n' + date[row][1].strip('\n')
    
       
    else :
        result = '※ ' + info + " 일정표 ※"
        querys = \
            "SELECT " + sentence1 + ", " + sentence2 + \
            " from " + sentence3 + \
            " where " + sentence2 + " LIKE " + "'%" + info + "%'"
        
        cur.execute(querys)
        date = cur.fetchall()
        if len(date) > 0 :
            for row in range(0, len(date)):
                result += '\n\n' + date[row][0].strip('\n') + '\n' + date[row][1].strip('\n')
        else :
            result = '학사일정엔 해당 검색 결과가 없어요ㅜㅜ'
    
    conn.close()

    return result
