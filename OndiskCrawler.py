import requests
from bs4 import BeautifulSoup as bs

contents = []

num = 2576
try:
    while num <= 26536:
        url = f'https://ondisk.co.kr/index.php?mode=customer&sm=jehu_list&doc=&search=&category=&p={num}'
        print(url)
        try:
            response = requests.get(url)    
            num += 1

            html_text = response.text
            soup = bs(html_text, 'html.parser')

            tr_list = soup.find('tbody').find_all('tr')

            for tr in tr_list:
                title = tr.find('td', 'subject').text
                print(title)
                contents.append(title)
        except Exception as e:
            print(e)
            try:
                response = requests.get(url)    
                num += 1

                html_text = response.text
                soup = bs(html_text, 'html.parser')

                tr_list = soup.find('tbody').find_all('tr')

                for tr in tr_list:
                    title = tr.find('td', 'subject').text
                    print(title)
                    contents.append(title)
            except Exception as e:
                print(e)


    with open('ondisk_2.txt', 'w', encoding='utf-8') as file:
        for c in contents:
            file.write(c)
            file.write("\n")
except Exception as e:
    print(e)
    with open('ondisk_2.txt', 'w', encoding='utf-8') as file:
        for c in contents:
            file.write(c)
            file.write("\n")