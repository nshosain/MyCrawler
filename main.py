import requests
from bs4 import BeautifulSoup

#takes article url
print('Enter Daily Star URL: ')
article = input()

#gets url
r = requests.get(article)

#get html code
soup = BeautifulSoup(r.text, 'html.parser')

#get's title of the article
ttl = soup.find('h1',  attrs={'itemprop': 'headline'})
title = ttl.string

#get's posted/edited time of the article
tme = soup.find('div', attrs={'class': 'small-text'})
time = tme.text

#get's body of the article
bdy = soup.find('div', attrs={'class': 'field-body view-mode-full'})
body = bdy.text

#array for the data collected
records = []
records.append((title, time, body))
print('Article Crawl Successful.')

#writes data to the csv file
import pandas as pd
df = pd.DataFrame(records, columns=['title', 'time', 'body'])
df.to_csv('DailyStar_ArticleDetails.csv', index=False, encoding='utf-8')

#confirmation
print('Data Write Successful')

