from django.shortcuts import render
from django.template.response import TemplateResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
import json
import pymysql
from . import haksa_db_to_view
from . import club_db_to_view
from . import restaurant_db_to_view
from . import classic_list
from . import day_list

t = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday','saturday','sunday']
today = datetime.today().weekday()
day = t[today]

startButton = ['오늘의 인기검색어','학사일정','배달음식','동아리','아주봇']
endButton = ['아주봇','처음으로']
clubButton = ['중앙동아리','소학회']

clubButton = ['중앙동아리', '소학회', '학과', '대학', '관심사','아주봇','처음으로']
majorButton = ['e-비즈니스 학과', '건설시스템공학과', '건축학과', '경영학과', '경제학과', '교통시스템공학과', '국어국문학과',
               '금융공학과', '기계공학과', '문화컨텐츠학과', '물리학과', '미디어학과', '불어불문학과', '사이버보안학과',
               '사학과', '사회학과', '산업공학과', '생명과학과', '소프트웨어학과', '수학과', '스포츠레저학과', '신소재공학과',
               '심리학과', '영어영문학과', '응용화학생명공학과', '전자공학과', '정치외교학과', '행정학과', '화학공학과',
               '화학과', '환경안전공학과']
univButton = ['간호대학', '경영대학', '공과대학', '국제학부', '사회과학대학', '약학대학', '의과대학', '인문대학',
              '자연과학대학', '정보통신대학']
hobbyButton = \
        ['MIDI', '검도', '게임개발', '경제', '공연', '광고', '권투', '기타', '농구', '독서토론', '등산', '로봇', '록',
         '만화', '문예창작', '미술', '바둑', '발명', '발표', '배드민턴', '볼링', '봉사', '분자생물학', '사물놀이', '사진',
         '사회과학', '서예', '수화', '스노우보드', '스쿼시', '시사', '실용음악', '야구', '야학', '연극', '영상', '영어',
         '영화', '오케스트라', '유도', '음악', '임용고시', '자전거', '종교', '창업', '천문', '체육', '축구', '춤', '컴퓨터',
         '탁구', '태권도', '테니스', '토론', '패러글라이딩', '풍물', '합창', '흑인음악', '힙합']
hobbyButton2 = \
        ['MIDI ', '검도 ', '광고 ', '권투 ', '기타 ', '농구 ', '등산 ', '로봇 ', '록 ',
         '미술 ', '바둑 ', '발명 ', '발표 ', '배드민턴 ', '볼링 ', '봉사 ', '사진 ',
         '서예 ', '스노우보드 ', '스쿼시 ', '시사 ', '실용음악 ', '야구 ', '야학 ', '연극 ', '영상 ', '영어 ',
         '영화 ', '유도 ', '음악 ', '자전거 ', '종교 ', '천문 ', '축구 ', '컴퓨터 ',
         '탁구 ', '태권도 ', '테니스 ', '패러글라이딩 ', '풍물 ', '합창 ', '흑인음악 ', '힙합 ']

def keyboard(request):
        day_list.init()
        return JsonResponse({
                'type' : 'buttons',
                'buttons' : startButton
        })

@csrf_exempt
def message(request):

        json_str = ((request.body).decode('utf-8'))
        json_data = json.loads(json_str)
        content_name = json_data['content']

        rank = str(classic_list.pull())

        day_rank = str(day_list.pull())
              
#############################################################################################################
        if content_name in ('오늘의 인기검색어','인기검색어','인기 검색어') :
                return JsonResponse({
                        'message' : {
                                'text' : day_rank + '\n\n' + '\n' + rank                      
                        },
                        'keyboard' : {
                                'type' : 'buttons',
                                'buttons' : endButton
                        }
                })
#############################################################################################################
        if content_name == '학사일정' :
                classic_list.push(content_name)
                day_list.push(content_name)
                return JsonResponse({
                        'message' : {
                                'text' : rank + '\n\n' + '어떤 일정이 궁금하세요?'
                        },
                        'keyboard' : {
                                'type' : 'buttons',
                                'buttons' : ['전체','시험','방학','휴일','수강신청 관련','행정신청','입학/졸업','개강','아주봇','처음으로']
                        }
                })
#############################################################################################################

        #전체 학사 일정
        if content_name in ('전체','전체학사일정','학사력'): 
              info = str(haksa_db_to_view.haksa_db(content_name))
              classic_list.push(content_name)
              day_list.push(content_name)
              return JsonResponse({
                      'message' : {
                              'text' : rank + '\n\n' + info
                      },
                      'keyboard' : {
                              'type' : 'buttons',
                              'buttons' : endButton
                      }
              })
#############################################################################################################

        #시험 및 성적 관련 일정    
        if content_name == '시험' :
                classic_list.push(content_name)
                day_list.push(content_name)
                return JsonResponse({
                        'message' : {
                                'text' : rank + '\n\n' + '학기를 선택해주세요.'
                        },
                        'keyboard' : {
                                'type' : 'buttons',
                                'buttons' : ['1학기','2학기','아주봇','처음으로']
                        }
                })

        # 시험 및 성적 관련 일정 
        if content_name in ('1학기','2학기','중간','중간고사','기말','기말고사','성적','성적입력','성적정정','공고'):
              info = str(haksa_db_to_view.haksa_db(content_name))
              classic_list.push(content_name)
              day_list.push(content_name)
              return JsonResponse({
                      'message' : {
                              'text' : rank + '\n\n' + info
                      },
                      'keyboard' : {
                              'type' : 'buttons',
                              'buttons' : endButton
                      }
              })
#############################################################################################################

        #수강신청 관련 일정
        elif content_name == '수강신청 관련':
                classic_list.push(content_name)
                day_list.push(content_name)
                return JsonResponse({
                        'message' : {
                                'text' : rank + '\n\n' + '수강 관련 목록입니다.'
                        },
                        'keyboard' : {
                                'type' : 'buttons',
                                'buttons' : ['예비수강','수강신청','수강정정','수강신청 포기','취득학점 포기','아주봇','처음으로']
                        }
                })
           
        #수강신청 관련 일정
        elif content_name in ('예비수강','수강신청','수강정정','수강신청 포기','취득학점 포기'):
                info = str(haksa_db_to_view.haksa_db(content_name))
                classic_list.push(content_name)
                day_list.push(content_name)
                return JsonResponse({
                        'message' : {
                                'text' : rank + '\n\n' + info
                        },
                        'keyboard' : {
                                'type' : 'buttons',
                                'buttons' : endButton
                        }
                })
#############################################################################################################
        # 방학
        elif content_name in ('방학','여름방학','겨울방학'):
                info = str(haksa_db_to_view.haksa_db(content_name))
                classic_list.push(content_name)
                day_list.push(content_name)
                return JsonResponse({
                        'message' : {
                                'text' : rank + '\n\n' + info
                        },
                        'keyboard' : {
                                'type' : 'buttons',
                                'buttons' : endButton
                        }
                })
#############################################################################################################
        # 휴일
        elif content_name in ('휴일','공휴일','쉬는날'):
                info = str(haksa_db_to_view.haksa_db(content_name))
                classic_list.push(content_name)
                day_list.push(content_name)
                return JsonResponse({
                        'message' : {
                                'text' : rank + '\n\n' + info
                        },
                        'keyboard' : {
                                'type' : 'buttons',
                                'buttons' : endButton
                        }
                })

#############################################################################################################
        # 입학식/졸업식
        elif content_name == '입학/졸업':
                classic_list.push(content_name)
                day_list.push(content_name)
                return JsonResponse({
                        'message' : {
                                'text' : rank + '\n\n' + '입학/졸업 관련 목록입니다.'
                        },
                        'keyboard' : {
                                'type' : 'buttons',
                                'buttons' : ['입학식(신·편입)','졸업식(학위 수여식)','아주봇','처음으로']
                        }
                })
        # 입학식/졸업식
        elif content_name in ('입학식','졸업식','입학식(신·편입)','졸업식(학위 수여식)'):
                info = str(haksa_db_to_view.haksa_db(content_name))
                classic_list.push(content_name)
                day_list.push(content_name)
                return JsonResponse({
                        'message' : {
                                'text' : rank + '\n\n' + info
                        },
                        'keyboard' : {
                                'type' : 'buttons',
                                'buttons' : endButton
                        }
                })           
#############################################################################################################
        #개강 일정
        elif content_name in ('개강','개강날짜','개강일정'): 
                info = str(haksa_db_to_view.haksa_db(content_name))
                classic_list.push(content_name)
                day_list.push(content_name)
                return JsonResponse({
                        'message' : {
                                'text' : rank + '\n\n' + info
                        },
                        'keyboard' : {
                                'type' : 'buttons',
                                'buttons' : endButton
                        }
        })
#############################################################################################################
        #행정신청 관련 일정
        elif content_name == '행정신청':
                classic_list.push(content_name)
                day_list.push(content_name)
                return JsonResponse({
                        'message' : {
                                'text' : rank + '\n\n' + '행정신청 관련 목록입니다.'
                        },
                        'keyboard' : {
                                'type' : 'buttons',
                                'buttons' : ['전과','학기등록','전공/졸업 신청','아주봇','처음으로']
                        }
                })
      
        #행정신청 관련 일정
        elif content_name in ('전과','전과신청','전과 신청'):
                info = str(haksa_db_to_view.haksa_db(content_name))
                classic_list.push(content_name)
                day_list.push(content_name)
                return JsonResponse({
                        'message' : {
                                'text' : rank + '\n\n' + info
                        },
                        'keyboard' : {
                                'type' : 'buttons',
                                'buttons' : endButton
                        }
                })

        #행정신청 관련 일정
        elif content_name in('학기등록','등록','학기 등록'):
                info = str(haksa_db_to_view.haksa_db(content_name))
                classic_list.push(content_name)
                day_list.push(content_name)
                return JsonResponse({
                        'message' : {
                                'text' : rank + '\n\n' + info
                        },
                        'keyboard' : {
                                'type' : 'buttons',
                                'buttons' : endButton
                        }
                })

        elif content_name in ('전공/졸업 신청','졸업유예','졸업연기','졸업 유예','졸업 연기','전공 변경','전공 취소','복수전공','부전공','연계전공'):
                info = str(haksa_db_to_view.haksa_db(content_name))
                classic_list.push(content_name)
                day_list.push(content_name)
                return JsonResponse({
                        'message' : {
                                'text' : rank + '\n\n' + info
                        },
                        'keyboard' : {
                                'type' : 'buttons',
                                'buttons' : endButton
                        }
                })
#############################################################################################################
        if content_name == '동아리':
                classic_list.push(content_name)
                day_list.push(content_name)
                return JsonResponse({
                        'message': {
                                'text': rank + '\n\n' + '동아리를 검색하실 방법을 선택해주세요.'
                        },
                        'keyboard': {
                                'type': 'buttons',
                                'buttons': clubButton
                        }
                })

        if content_name == '중앙동아리':
                classic_list.push(content_name)
                day_list.push(content_name)
                return JsonResponse({
                        'message': {
                                'text': rank + '\n\n' + '중앙동아리 내에서 검색'
                        },
                        'keyboard': {
                                'type': 'buttons',
                                'buttons': ['중앙동아리 전체', '관심사별 조회','아주봇','처음으로']
                        }
                })

        if content_name == '중앙동아리 전체':
                info = str(club_db_to_view.club(content_name))
                classic_list.push(content_name)
                day_list.push(content_name)
                return JsonResponse({
                        'message': {
                                'text': rank + '\n\n' + info
                        },
                        'keyboard': {
                                'type': 'buttons',
                                'buttons': endButton
                        }
                })

        if content_name == '관심사별 조회':
                classic_list.push(content_name)
                day_list.push(content_name)
                return JsonResponse({
                        'message': {
                                'text': rank + '\n\n' + '중동 내 관심사를 선택해 주세요'
                        },
                        'keyboard': {
                                'type': 'buttons',
                                'buttons': hobbyButton2
                        }
                })

        # 중동 - 관심사별 조회 선택시
        elif content_name in hobbyButton2:
                info = str(club_db_to_view.club(content_name))
                classic_list.push(content_name)
                day_list.push(content_name)
                return JsonResponse({
                        'message': {
                                'text': rank + '\n\n' + info
                        },
                        'keyboard': {
                                'type': 'buttons',
                                'buttons': endButton
                        }
                })

        if content_name == '소학회':
                info = str(club_db_to_view.club(content_name))
                classic_list.push(content_name)
                day_list.push(content_name)
                return JsonResponse({
                        'message': {
                                'text': rank + '\n\n' + info
                        },
                        'keyboard': {
                                'type': 'buttons',
                                'buttons': endButton
                        }
                })

        if content_name == '학과':
                classic_list.push(content_name)
                day_list.push(content_name)
                return JsonResponse({
                        'message': {
                                'text': rank + '\n\n' + '학과를 선택해 주세요'
                        },
                        'keyboard': {
                                'type': 'buttons',
                                'buttons': majorButton
                        }
                })

        # 학과 선택시
        elif content_name in majorButton:
                info = str(club_db_to_view.club(content_name))
                classic_list.push(content_name)
                day_list.push(content_name)
                return JsonResponse({
                        'message': {
                                'text': rank + '\n\n' + info
                        },
                        'keyboard': {
                                'type': 'buttons',
                                'buttons': endButton
                        }
                })

        if content_name == '대학':
                classic_list.push(content_name)
                day_list.push(content_name)
                return JsonResponse({
                        'message': {
                                'text': rank + '\n\n' + '대학을 선택해 주세요'
                        },
                        'keyboard': {
                                'type': 'buttons',
                                'buttons': univButton
                        }
                })

        # 대학 선택시
        elif content_name in univButton:
                info = str(club_db_to_view.club(content_name))
                classic_list.push(content_name)
                day_list.push(content_name)
                return JsonResponse({
                        'message': {
                                'text': rank + '\n\n' + info
                        },
                        'keyboard': {
                                'type': 'buttons',
                                'buttons': endButton
                        }
                })

        if content_name == '관심사':
                classic_list.push(content_name)
                day_list.push(content_name)
                return JsonResponse({
                        'message': {
                                'text': rank + '\n\n' + '관심사를 선택해 주세요'
                        },
                        'keyboard': {
                                'type': 'buttons',
                                'buttons': hobbyButton
                        }
                })

        # 관심사 선택시
        elif content_name in hobbyButton:
                info = str(club_db_to_view.club(content_name))
                classic_list.push(content_name)
                day_list.push(content_name)
                return JsonResponse({
                        'message': {
                                'text': rank + '\n\n' + info
                        },
                        'keyboard': {
                                'type': 'buttons',
                                'buttons': endButton
                        }
                })
#############################################################################################################
        #음식점
        elif content_name == '배달음식' :
                classic_list.push(content_name)
                day_list.push(content_name)
                info = str(restaurant_db_to_view.pull_rate(day))
                return JsonResponse({
                        'message': {
                                'text': info + '\n\n' + '원하시는 종류를 선택해주세요.'
                        },
                        'keyboard': {
                                'type': 'buttons',
                                'buttons': ['한식','중식','일식','치킨','피자','햄버거']
                        }
                })
        
        elif content_name == '한식' :
                restaurant_db_to_view.push_count(content_name)
                return JsonResponse({
                        'message': {
                                'text': '원하시는 음식점을 선택해주세요.'
                        },
                        'keyboard': {
                                'type': 'buttons',
                                'buttons': ['삼겹데이','호세야오리바베큐','곱창','황금벼슬찜닭','미스터통삽겹']
                        }
                })

        elif content_name == '중식' :
                restaurant_db_to_view.push_count(content_name)
                return JsonResponse({
                        'message': {
                                'text': '원하시는 음식점을 선택해주세요.'
                        },
                        'keyboard': {
                                'type': 'buttons',
                                'buttons': ['짜장마을','영빈반점','리향','궁차이나','짬뽕이좋아']
                        }
                })
                
        elif content_name == '일식' :
                restaurant_db_to_view.push_count(content_name)
                return JsonResponse({
                        'message': {
                                'text': '원하시는 음식점을 선택해주세요.'
                        },
                        'keyboard': {
                                'type': 'buttons',
                                'buttons': ['키와마루아지','소고','가츠스시','만고쿠','화산']
                        }
                })
                
        elif content_name == '치킨' :
                restaurant_db_to_view.push_count(content_name)
                return JsonResponse({
                        'message': {
                                'text': '원하시는 음식점을 선택해주세요.'
                        },
                        'keyboard': {
                                'type': 'buttons',
                                'buttons': ['순살파닭','마시내순살파닭','코리엔탈깻잎치킨','굽네치킨','원+원치킨']
                        }
                })

        elif content_name == '피자' :
                restaurant_db_to_view.push_count(content_name)
                return JsonResponse({
                        'message': {
                                'text': '원하시는 음식점을 선택해주세요.'
                        },
                        'keyboard': {
                                'type': 'buttons',
                                'buttons': ['클래식임실피자','임실치즈피자','헤레스임실피자','토마토피자','피자헤븐']
                        }
                })

        elif content_name == '햄버거' :
                restaurant_db_to_view.push_count(content_name)
                return JsonResponse({
                        'message': {
                                'text': '원하시는 음식점을 선택해주세요.'
                        },
                        'keyboard': {
                                'type': 'buttons',
                                'buttons': ['맘스터치','롯데리아','KFC','맥도날드','버거킹']
                        }
                })

#############################################################################################################
        if content_name == '아주봇' :
                return JsonResponse({
                        'message' : {
                                'text' : rank + '\n\n' + '아주대에 관해 모르는거 빼고 다 알아요!'
                        },
                        'keyboard' : {
                                'type' : 'text'
                        }
                })


        if content_name == '처음으로' :
                return JsonResponse({
                	'message' : {
                		'text' : rank + '\n\n' + '처음으로 돌아갑니다.'
                	},
                        'keyboard' : {
                                'type' : 'buttons',
                                'buttons' : startButton
                        }
                })              

        else :
                info = str(haksa_db_to_view.haksa_db(content_name))
                info2 = str(club_db_to_view.club(content_name))
                info3 = str(restaurant_db_to_view.pull_info(content_name))
                classic_list.push(content_name)
                day_list.push(content_name)
                return JsonResponse({ 
                        'message' : {
                                'text' : rank + '\n\n' + info + '\n' + info2 + '\n' + info3 + '\n'
                        },
                        'keyboard' : {
                                'type' : 'buttons',
                                'buttons' : startButton
                        }
                })


