from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from bs4 import BeautifulSoup as bs

options = webdriver.ChromeOptions()
options.add_argument(("lang=ko_KR"))
options.add_experimental_option('excludeSwitches', ['enable-logging'])
# 브라우저 창 사이즈
options.add_argument('window-size=1280x720')

# 드라이버 경로 입력
s = Service('chromedriver.exe')
driver = webdriver.Chrome(service=s, options=options)
wait = WebDriverWait(driver, 10)

contents = []
state = True
try:
    num = 0
    while state:
        driver.get(f'https://www.applefile.com/company/#tab=copyright_list&pn={num}')
        driver.implicitly_wait(3)
        print(f'https://www.applefile.com/company/#tab=copyright_list&pn={num}')
        num += 1

        try:
            html = driver.page_source
            soup = bs(html, 'html.parser')

            tr_list = soup.find('tbody').find_all('tr')

            for tr in tr_list:
                td = tr.find_all('td')
                if td[0].text == "데이터가 없습니다.":
                    print("데이터가 없습니다. 크롤링을 종료합니다.")
                    state = False
                    break

                title = td[1].text
                cp = td[2].text

                print(f'{title}\t{cp}')

                contents.append(f'{title}\t{cp}\n')
        except:
            try:
                time.sleep(1)

                print("재탐색합니다.")

                html = driver.page_source
                soup = bs(html, 'html.parser')

                tr_list = soup.find('tbody').find_all('tr')

                for tr in tr_list:
                    td = tr.find_all('td')
                    if td[0].text == "데이터가 없습니다.":
                        print(td[0].text)
                        state = False
                        break

                    title = td[1].text
                    cp = td[2].text

                    print(f'{title}\t{cp}')

                    contents.append(f'{title}\t{cp}\n')
            except Exception as e:
                print(e)

    with open('applefile.txt', 'w', encoding='utf-8') as file:
        for c in contents:
            file.write(c)
except Exception as e:
    print(e)
    with open('applefile.txt', 'w', encoding='utf-8') as file:
        for c in contents:
            file.write(c)

