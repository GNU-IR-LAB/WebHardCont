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

driver.get('https://www.filecity.co.kr/')
driver.implicitly_wait(3)

# 로그인
driver.find_element(By.XPATH, '//*[@id="userid"]').send_keys('ooo5094')
driver.find_element(By.XPATH, '//*[@id="userpw"]').send_keys('g221124104!')
driver.find_element(By.XPATH, '//*[@id="login_form"]/div/div[3]/div/ul[2]/li[2]/input').click()
time.sleep(1)

alert = driver.switch_to.alert
alert.accept()

contents = []
try:
    num = 30156
    while num <= 45539:
        driver.get(f'https://dev.filecity.co.kr/customer/#tab=4&pn={num}')
        print(f'https://dev.filecity.co.kr/customer/#tab=4&pn={num}')
        #time.sleep(1)
        num += 1

        html = driver.page_source
        soup = bs(html, 'html.parser')
        try:
            table = soup.find('table', {id:'list'})
            tr_list = table.find_all('tr')[1:]

            for tr in tr_list:
                title = tr.find('td', 'al_left').find('span').text
                contents.append(f'{title}')
                print(title)
        except:
            try:
                time.sleep(1)

                print("재탐색합니다.")
                table = soup.find('table')
                tr_list = table.find_all('tr')[1:]

                for tr in tr_list:
                    title = tr.find('td', 'al_left').find('span').text 
                    contents.append(f'{title}')
                    print(title)
            except:
                pass
    with open('filecity.txt', 'a', encoding='utf-8') as file:
        for c in contents:
            file.write(c)
except Exception as e:
    print(e)
    with open('filecity.txt', 'a', encoding='utf-8') as file:
        for c in contents:
            file.write(c)

