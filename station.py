import requests
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

def station():
    url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query='
    station = ''

    # #사용자에게 입력받은 값으로 역 설정
    while 1:
        num = input("정왕역 = 1 / 오이도역 = 2")
        if num == "1" :
            station = "정왕역막차"
            break
        elif num == "2" :
            station = "수인선오이도역막차"
            break
        else :
            print("잘못 입력했어요. 다시 입력하세요.")

    url += station 
    dr = webdriver.Chrome()
    dr.get(url)
    time.sleep(1)
    tbody = dr.find_element(By.TAG_NAME, "tbody")
    inner_timeline = tbody.find_elements(By.CLASS_NAME,"inner_timeline")
    for i in range(len(inner_timeline)):
        str1 = ''
        try:
            wrap_time = inner_timeline[i].find_element(By.CLASS_NAME,"wrap_time")
            wrap_station = inner_timeline[i].find_element(By.CLASS_NAME, "wrap_station")
            tm = wrap_time.find_element(By.CLASS_NAME,"time").text
            st = wrap_station.find_elements(By.TAG_NAME,"em")
            str1 += tm + ' ' + st[0].text + '->' +  st[1].text
            print(str1)
            print()
        except NoSuchElementException as e:
            str1 += ''
            print(str1)
            print()
    dr.quit()


    #     print("정왕역 막차 정보입니다!")
    #     print("종 착 역  / 평 일 /  주말 및 공휴일")
    #     print("당고개행 :", text_4_sta[5], text_4_sta[6])
    #     print("사 당 행 :", text_4_sta[13], text_4_sta[14])
    #     print("금 정 행 :", text_4_sta[17], text_4_sta[18])
    #     print("오이도행 :", text_su_sta[11], text_su_sta[12])
    #     print("본 정보는 네이버 검색 결과를 바탕으로 제공됩니다.")
    # elif station == '수인선오이도역막차' :
    #     table_div = soup.find_all("tr", {"class" : "last"})
    #     table_tr = table_div[1]

    #     text_su_sta = []
    #     for item in table_tr :
    #         if item != " " :
    #             text_su_sta += item

    #     text_sta = []
    #     for item in text_su_sta :
    #         text_sta += item

    #     print("오이도역(수인선) 막차 정보입니다!")
    #     print("종 착 역  / 평 일 /  주말 및 공휴일")
    #     print("인 천 행 :", text_sta[1], text_sta[2])
    #     print("본 정보는 네이버 검색 결과를 바탕으로 제공됩니다.")
station()

