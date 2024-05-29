import requests  # HTTP 요청을 보내기 위한 라이브러리
import time  # 시간 관련 기능을 제공하는 모듈
from selenium import webdriver  # 웹 브라우저 자동화를 위한 라이브러리
from selenium.common.exceptions import NoSuchElementException  # 셀레니움에서 발생하는 예외 처리
from selenium.webdriver.chrome.service import Service  # 크롬 드라이버 서비스를 설정하기 위한 모듈
from selenium.webdriver.common.keys import Keys  # 키보드 입력을 시뮬레이션하기 위한 모듈
from selenium.webdriver.common.by import By  # HTML 요소를 찾기 위한 모듈
from bs4 import BeautifulSoup  # HTML 및 XML 구문 분석을 위한 라이브러리
from datetime import datetime  # 날짜 및 시간 관련 기능을 제공하는 모듈


def station(num):
    url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query='
    station = ''

    # 사용자에게 입력받은 값으로 역 설정
    while True:
        if num == "1":
            station = "정왕역막차"
            break
        elif num == "2":
            station = "정왕역수인분당선막차"
            break
        else:
            print("잘못 입력했어요. 다시 입력하세요.")

    last_canival = []  # 막차 정보를 저장할 리스트
    url += station  # URL에 역 정보를 추가
    now = datetime.now()  # 현재 시간 정보를 가져옴
    dr = webdriver.Chrome()  # 크롬 드라이버를 사용하여 브라우저를 실행
    dr.get(url)  # 설정한 URL로 이동
    time.sleep(3.5)  # 페이지 로드 대기
    source = dr.page_source  # 페이지 소스를 가져옴
    bs = BeautifulSoup(source, 'lxml')  # 페이지 소스를 파싱하여 BeautifulSoup 객체 생성
    station_time = bs.find_all('strong', {'class': 'time'})  # 시간 정보를 가져옴
    station_lines = bs.find_all('em', {'class': 'station'})  # 역 정보를 가져옴

    cnt = 0  # 막차 정보를 두 개까지 저장하기 위한 카운트 변수
    cout_cnt = 0  # 출력된 막차 정보의 개수를 세기 위한 변수
    j = 0  # 역 정보를 순차적으로 접근하기 위한 인덱스 변수

    for tm in range(len(station_time)):
        st_tms = station_time[tm].get_text()  # 시간 정보를 텍스트로 가져옴
        st_tm = [int(st_tms[0:2]), int(st_tms[3:5])]  # 시간과 분을 정수형으로 변환하여 리스트에 저장
        if int(st_tms[0:2]) == 0:
            st_tm[0] = 24  # 00시를 24시로 변환

        # 특정 방향의 역을 건너뛰기 위한 조건
        if station_lines[j].get_text() == '당고개' or station_lines[j].get_text() == '왕십리':
            j += 2
            continue
        # 현재 시간보다 이전의 시간 정보를 건너뛰기 위한 조건
        elif st_tm[0] < now.hour or (st_tm[0] == now.hour and st_tm[1] < now.minute):
            j += 2
            continue
        else:
            if cnt == 2:
                break
            else:
                # 막차 정보를 리스트에 추가
                last_canival.append(
                    station_time[tm].get_text() + " " + station_lines[j].get_text() + ' -> ' + station_lines[
                        j + 1].get_text())
                j += 2
                cout_cnt += 1
                cnt += 1

    dr.quit()  # 브라우저를 종료

    return last_canival  # 막차 정보 리스트 반환
