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
        num = input("정왕역(4호선) = 1 / 정왕역(수인분당선) = 2")
        if num == "1" :
            station = "정왕역막차"
            break
        elif num == "2" :
            station = "정왕역수인분당선막차"
            break
        else :
            print("잘못 입력했어요. 다시 입력하세요.")

    url += station 
    dr = webdriver.Chrome()
    dr.get(url)
    time.sleep(1)
    tbody = dr.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/div[1]/section[1]/div[2]/div/div[1]/div/div[5]/div[2]/div/div[3]/table/tbody")
    inner_timeline = tbody.find_elements(By.CLASS_NAME,"inner_timeline")
    time_list = []
    station_list = []
    for i in range(len(inner_timeline)):
        str_example = ''
        try:
            wrap_time = inner_timeline[i].find_element(By.CLASS_NAME,"wrap_time")
            wrap_station = inner_timeline[i].find_element(By.CLASS_NAME, "wrap_station")
            tm = wrap_time.find_element(By.CLASS_NAME,"time").text
            st = wrap_station.find_elements(By.TAG_NAME,"em")
            str_example += tm + ' ' + st[0].text + ' -> ' +  st[1].text
            time_list.append(tm)
            station_list.append([st[0].text,st[1].text])
            if station == '정왕역막차':
                print("정왕역 막차 정보입니다!")
                print()
            else:
                print("수인선 오이도역 막차 정보입니다!")
                print()
            print(str_example)
            print("본 정보는 네이버 검색 결과를 바탕으로 제공됩니다.")
            print()
        except NoSuchElementException as e:
            print()
    #print(time_list, ' ' , station_list)
    dr.quit()