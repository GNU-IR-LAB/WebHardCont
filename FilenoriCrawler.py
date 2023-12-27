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

import sys
import re

start = 0
end = 0
if len(sys.argv) == 3:
    start = int(sys.argv[1])
    end = int(sys.argv[2])
else:
    print("인수가 부족하거나 너무 많습니다.")
    sys.exit()

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
    tr_list = soup.find('tbody').find_all('tr')
    if len(tr_list) == 0:
        print("컨텐츠 없음.")
        return False
    for tr in tr_list:
        td = tr.find_all('td')

        title = td[1].find('div').text.replace('\t', '').replace('\n', '')
        ep = td[2].text.replace('\t', '').replace('\n', '')

        if (title.find(ep+'회') > -1) or (title.find(ep+'화') > -1) or (td[0].text == '영화'):
            contents.append(f'{title}\n')
            print(f'"{title}"')
        else:
            contents.append(f"{title} {ep}화\n")
            print(f'"{title}" {ep}화')
    return True

try:
    num = start
    state = True
    #25061
    while state or num <= end:
        driver.get(f'http://www.filenori.com/noriNew/Support/popupCprContentsList.do?pageViewPoint={num}')
        print(driver.current_url)
        #time.sleep(1)
        num += 1

        try:
            html = driver.page_source
            state = content_find(html)
        except:
            try:
                time.sleep(1)
                print("재탐색합니다.")
                state = content_find(html)
            except:
                pass
    with open(f'filenori_{start}_{end}.txt', 'a', encoding='utf-8') as file:
        for c in contents:
            file.write(c)
    print("크롤링 종료.")
except Exception as e:
    print(e)
    with open(f'filenori_{start}_{end}.txt', 'a', encoding='utf-8') as file:
        for c in contents:
            file.write(c)
