#https://smartfile.co.kr/copy/copy_06.htm?stx=&wr_subject=&page=1
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

contents = []

def content_find(html):
    soup = bs(html, 'html.parser')

    tr_list = soup.find('tbody').find_all('tr')
    if len(tr_list) == 0:
        return False
    for tr in tr_list:
        td = tr.find_all('td')
        title = td[2].text
        copy = td[3].text

        contents.append(f'{title}\t{copy}\n')
        print(f'{title}\t{copy}')
    return True
try:
    num = 1
    while True:
        url = f'https://smartfile.co.kr/copy/copy_06.htm?stx=&wr_subject=&page={num}'
        print(url)
        num +=1
        
        try:
            response = requests.get(url)    
            html_text = response.text
            result = content_find(html_text)
            if not result:
                print("데이터 없음.")
                break
        except Exception as e:
            print(e)
            try:
                response = requests.get(url)    
                html_text = response.text
                result = content_find(html_text)
            except Exception as e:
                print(e)
        
    
    with open('smartfile.txt', 'a', encoding='utf-8') as file:
        for c in contents:
            file.write(c)
    print("크롤링 종료")
except Exception as e:
    print(e)
    with open('smartfile.txt', 'a', encoding='utf-8') as file:
        for c in contents:
            file.write(c)