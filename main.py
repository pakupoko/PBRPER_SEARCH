# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 18:05:30 2019

@author: tjlee
"""

'''main.py -> 주요 UI 출력. 종목 검색 기능만, 없는 종목일 경우 '없는 종목입니다'를 띄울것
crawling.py에서 해당 값을 추출한 후 main.py에서 띄울 것
''' 
'''
crawling_pbrper.py -> 해당 종목 사이트로 이동, PBR, PER 획득
crawling_icr.py-> 이자보상배율 정보 획득 및 출력 
'''

from crawling import crawling_icr, crawling_perpbr

while True:
    cd_num=input("원하시는 명령을 선택해주세요(1-투자정보 확인, 2-참고 사이트 링크, 0-종료) : ")
    
    if not cd_num in ['1','2','0']:
        print("잘못된 입력입니다. 다시 입력해주세요.")
    elif cd_num == '1' :
        cd_num2=input('종목코드를 입력하세요 : ')
        #perpbr 검색 모듈 호출 
        crawling_perpbr.crawling_perpbr(cd_num2)
        #이자보상배율 검색 모듈 호출 
        crawling_icr.crawling_icr(cd_num2)
    elif cd_num == '2' :
        print('네이버 금융 : https://finance.naver.com/')
        print('CompanyGuide : http://comp.fnguide.com/SVO2/asp/SVD_Main.asp')
    elif cd_num == '0':
        print('종료')
        break
    
    






