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
    table = soup.select_one('#subBody > table > tbody > tr:nth-child(2) > td:nth-child(2) > table > tbody > tr:nth-child(5) > td > table')
    tr_list = table.find_all('tr')[4:-1]
    for tr in tr_list:
        td = tr.find_all('td')
        if len(td) > 1:
            title = td[1].text.replace('\t', '').replace('\n', '')
            copy = td[2].text.replace('\t', '').replace('\n', '')
            state = td[3].text
            if state == '진행':
                contents.append(f"{title}\t{copy}\n")
                print(f'{title}')


try:
    num = 1

    #17302
    while num<=17302:
        driver.get(f'https://www.bigfile.co.kr/customer/customer_cp_content.php?p_page={num}')
        print(driver.current_url)
        #time.sleep(1)
        num += 1

        try:
            html = driver.page_source
            content_find(html)
        except Exception as e:
            try:
                print(e)
                time.sleep(1)
                print("재탐색합니다.")
                #content_find(html)
            except:
                pass
    with open('bigfile.txt', 'a', encoding='utf-8') as file:
        for c in contents:
            file.write(c)
    print("크롤링 종료.")
except Exception as e:
    print(e)
    with open('bigfile.txt', 'a', encoding='utf-8') as file:
        for c in contents:
            file.write(c)
