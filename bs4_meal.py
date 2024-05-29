import requests  # HTTP 요청을 보내기 위한 라이브러리
from bs4 import BeautifulSoup  # HTML 및 XML 구문 분석을 위한 라이브러리
import os  # 운영체제와 상호작용하기 위한 모듈


def get_meal():
    # 학식 정보를 가져올 URL과 헤더 설정
    url = "https://ibook.kpu.ac.kr/Viewer/menu02"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    }

    # 첫 번째 요청: 메인 페이지에서 bookcode를 추출
    req = requests.get(url, headers=headers)  # 지정한 URL에 GET 요청을 보냄
    soup = BeautifulSoup(req.text, 'lxml')  # 응답 텍스트를 BeautifulSoup 객체로 파싱
    bookcode = soup.find(attrs={"name": "bookcode"}).get("value")  # name 속성이 'bookcode'인 요소를 찾아 value 속성 값을 추출

    # 두 번째 요청: 추출한 bookcode를 사용하여 XML 데이터 가져오기
    req = requests.get(f"https://ibook.kpu.ac.kr/Viewer/getBookXML/{bookcode}",
                       headers=headers)  # bookcode를 포함한 URL에 GET 요청
    json_data = req.json()  # 응답을 JSON 형식으로 파싱
    srcs = [json_data[0]['src'], json_data[1]['src']]  # 첫 번째와 두 번째 이미지 소스 URL을 리스트로 추출
    path = os.path.dirname(os.path.abspath(__file__))  # 현재 파일의 디렉토리 경로를 가져옴

    # 각 이미지 URL에 접근하여 이미지를 다운로드 및 저장
    for i in range(len(srcs)):
        imgurl = "https:" + srcs[i]  # 이미지 URL 완성
        req = requests.get(imgurl, headers=headers)  # 이미지 URL에 GET 요청을 보내서 이미지 데이터 가져옴
        with open(os.path.join(path, f"{i}.jpg"), "wb") as f:  # 현재 디렉토리에 0.jpg, 1.jpg로 저장
            f.write(req.content)  # 응답의 콘텐츠(이미지 데이터)를 파일에 기록
