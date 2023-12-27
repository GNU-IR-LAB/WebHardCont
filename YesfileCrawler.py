# try:
#     num = 0
#     while num<=25061:
#         url = f'https://www.filesun.com/disk/popup_copylist?page={num}'
#         print(url)
#         num +=1
        
#         try:
#             content_find(url)
#         except Exception as e:
#             print(e)
#             try:
#                 content_find(url)
#             except Exception as e:
#                 print(e)
        

#     with open('yesfile.txt', 'a', encoding='utf-8') as file:
#         for c in contents:
#             file.write(c)
#     print("크롤링 종료")
# except Exception as e:
#     print(e)
#     with open('yesfile.txt', 'a', encoding='utf-8') as file:
#         for c in contents:
#             file.write(c)

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.alert import Alert


options = webdriver.ChromeOptions()
options.add_argument(("lang=ko_KR"))
options.add_experimental_option('excludeSwitches', ['enable-logging'])
# options.add_extension('bihmplhobchoageeokmgbdihknkjbknd.crx')

# 브라우저 창 사이즈
options.add_argument('window-size=1280x720')

# 드라이버 경로 입력
s = Service('chromedriver.exe')
driver = webdriver.Chrome(service=s, options=options)
wait = WebDriverWait(driver, 10)

contents = []

def content_find(html):
    soup = bs(html, 'html.parser')

    table = soup.find('tbody')

    trs = table.find_all('tr')

    for tr in trs:
        title = tr.find('td', 'tal').text
        copyright = tr.find_all('td', 'color_g')[2].text

        contents.append(f'{title}\t{copyright}\n')
        print(f'{title}\t{copyright}\n')

try:
    num = 1
    #25061
    while num <= 25061:
        driver.get(f'https://www.yesfile.com/company/#tab=6&tab2=1&s_type=&s_title=&pn={num}')
        print(f'https://www.yesfile.com/company/#tab=6&tab2=1&s_type=&s_title=&pn={num}')
        #time.sleep(1)
        num += 1

        try:
            html = driver.page_source
            content_find(html)
        except:
            try:
                time.sleep(1)

                print("재탐색합니다.")
                content_find(html)
            except:
                pass
    with open('yesfile.txt', 'a', encoding='utf-8') as file:
        for c in contents:
            file.write(c)
except Exception as e:
    print(e)
    with open('yesfile.txt', 'a', encoding='utf-8') as file:
        for c in contents:
            file.write(c)

