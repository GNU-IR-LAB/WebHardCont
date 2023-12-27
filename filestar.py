import requests
from bs4 import BeautifulSoup as bs

contents = []

try:
    num = 1
    while True:
        url = f'https://filestar.co.kr/copyright/page/6?page={num}'
        print(url) 
        num += 1

        response = requests.get(url)    

        html_text = response.text


        soup = bs(html_text, 'html.parser')


        li = soup.find('ul', 'list_style').find_all('li')[1:]
        if not li:
            break

        for l in li:
            title = l.find_all('span', 'tit')
            com = l.find_all('div', 'l3')

            for i in range(len(title)):
                contents.append([title[i].text, com[i].find('span').text])
                print(title[i].text)

    with open('filestar.txt', 'w', encoding='utf-8') as file:
        for c in contents:
            file.write(c[0] + "\t" + c[1] + "\n")
except:
    with open('filestar.txt', 'w', encoding='utf-8') as file:
        for c in contents:
            file.write(c[0] + "\t" + c[1] + "\n")
