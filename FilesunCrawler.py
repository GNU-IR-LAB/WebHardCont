import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

contents = []
state = True

def content_find(url):
    response = requests.get(url)    

    html_text = response.text
    soup = bs(html_text, 'html.parser')

    table = soup.find('tbody')

    trs = table.find_all('tr')

    for tr in trs:
        number = tr.find('td', 'number').text
        if int(number) == 0:
            return False
        title = tr.find('td', 'subject').text
        ep = tr.find('td', 'vcEpisode').text
        copyright = tr.find('td', 'copyright').text
        print(number + ": " + title)
        
        if int(ep) <= 1:
            contents.append(f'{title}\t{copyright}')
        else:
            contents.append(f'{title} {ep}화\t{copyright}')
    return True

try:
    num = 1753
    while state:
        url = f'https://www.filesun.com/disk/popup_copylist?page={num}'
        print(url)
        num +=1
        
        try:
            state = content_find(url)
        except Exception as e:
            print(e)
            try:
                state = content_find(url)
            except Exception as e:
                print(e)
        
    
    with open('filesun_3.txt', 'w', encoding='utf-8') as file:
        for c in contents:
            file.write(c)
            file.write("\n")
    print("크롤링 종료")
except Exception as e:
    print(e)
    with open('filesun_3.txt', 'w', encoding='utf-8') as file:
        for c in contents:
            file.write(c)
            file.write("\n")