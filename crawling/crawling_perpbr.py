# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 18:15:23 2019

@author: tjlee
"""
import requests
from bs4 import BeautifulSoup

def crawling_perpbr(cd):
    #URL 설정
    try: #에러 검출
        NAVER_FINANCE_SEARCH_URL='https://finance.naver.com/item/main.nhn?'
        
        
        params = {
                'code' : cd 
                }
        
        #URL 태그 추출
        resp = requests.get(NAVER_FINANCE_SEARCH_URL, params=params)
        soup = BeautifulSoup(resp.content, 'html.parser')
        
        
        #기업명 추출 
        title_contents=soup.find(attrs={'class':'wrap_company'}).find('h2')
        
        #per 테이블 추출 
        per_contents=soup.find(attrs={'class' : 'aside_invest_info'}).find(attrs={'class' : 'per_table'})
        em_contents=per_contents.find_all('em')
        
        #per 내 값들 추출 
        
        temp_list=[]
        for em in em_contents:
            temp_list.append(em.text)
            
        
        print(title_contents.text)  
        print(f"PER : {temp_list[0]}배 | EPS : {temp_list[1]}원\nPER(krx) : {temp_list[2]}배 | EPS(krx) : {temp_list[3]}원\n추정PER : {temp_list[4]}배 | 추정EPS : {temp_list[5]}원\nPBR : {temp_list[6]}배 | BPS : {temp_list[7]}원\n배당수익률 : {temp_list[8]}%")
        
        
    except Exception as e:
        print(e)
        print("에러")

        
        

