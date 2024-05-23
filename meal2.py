#pip install BeautifulSoup4 lxml

import requests
from bs4 import BeautifulSoup
import os
from PIL import Image
import time

url = "https://ibook.kpu.ac.kr/Viewer/menu02"
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"}
req = requests.get(url, headers=headers)
soup = BeautifulSoup(req.text, 'lxml')
bookcode = soup.find(attrs={"name":"bookcode"}).get("value")

req = requests.get(f"https://ibook.kpu.ac.kr/Viewer/getBookXML/{bookcode}", headers=headers)
srcs = [req.json()[0]['src'], req.json()[1]['src']]
path = os.path.dirname(os.path.abspath(__file__))

for i in range(0, len(srcs)):
        file_path = f'{i}.jpg'

    if os.path.exists(file_path):
        os.remove(file_path)
    time.sleep(1)

    imgurl = "https:" + srcs[i]
    req = requests.get(imgurl, headers=headers)
    with open(os.path.join(path, f"{i}.jpg"), "wb") as f:
        f.write(req.content)   
    img = Image.open(f'{i}.jpg')
    img.show()     
