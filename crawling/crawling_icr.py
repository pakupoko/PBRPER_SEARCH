# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 16:06:52 2019

@author: tjlee
"""

import requests
from bs4 import BeautifulSoup

def crawling_icr(cd):
    #URL 설정
    try:
        FNGUIDE_FINANCE_SEARCH_URL=f'http://comp.fnguide.com/SVO2/asp/SVD_FinanceRatio.asp?pGB=5&gicode=A{cd}&cID=&MenuYn=N&ReportGB=&NewMenuID=104&stkGb=701'
        
        #URL 태그 추출
        resp = requests.get(FNGUIDE_FINANCE_SEARCH_URL)
        soup = BeautifulSoup(resp.content, 'html.parser')
        
        #이자보상배율 데이터 추출
        tr_contents=soup.find_all('tr')
        
        temp_data=''
        for tr in tr_contents:
            if tr.text.find('이자보상배율') != -1:
                temp_data=tr.text
                break
        
        print(f'이자보상배율 : {temp_data.split()[-1]}')
    except Exception as e:
        print(e)
        print('에러')

    

        