import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

contents = []

num = 1
url = f'https://www.filesun.com/'

response = requests.get(url)    

print(response)
# html_text = response.text
# soup = bs(html_text, 'html.parser')

# table = soup.find('tbody')

# trs = table.find_all('tr')

# for tr in trs:
#     title = tr.find('td', 'subject').text
#     ep = tr.find('td', 'vcEpisode').text
#     copyright = tr.find('td', 'copyright').text
#     if int(ep) <= 1:
#         contents.append(f'{title}\t{copyright}')
#     else:
#         contents.append(f'{title} {ep}화\t{copyright}')

# with open('filestar.txt', 'w', encoding='utf-8') as file:
#     for c in contents:
#         file.write(c)