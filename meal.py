import requests
import time
import os
from urllib.request import urlretrieve
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

def meal():
    url = 'https://ibook.kpu.ac.kr/Viewer/menu02'
    
    dr = webdriver.Chrome()
    dr.get(url)
    time.sleep(0.5)
    img1 = dr.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div[1]/div/div/img")
    img2 = dr.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div[3]/div/div/img')
    meal_text = [img1.get_attribute("src"),img2.get_attribute("src")]
    #print(meal_text)
    path_folder = "C:/Users/ywysg/Desktop/Shool_meal/meal_img"
    with open("meal_tip.jpg","wb") as f:
        f.write(requests.get(meal_text[0]).content)
    with open("meal_E.jpg","wb") as f:
        f.write(requests.get(meal_text[1]).content)
    dr.quit()