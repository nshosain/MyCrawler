import requests
from bs4 import BeautifulSoup

#takes article url
print('Enter Prothom Alo URL (En): ')
article = input()

#gets url
r = requests.get(article)

#get html code
soup = BeautifulSoup(r.text, 'html.parser')

#gets title of the article
ttl = soup.find('h1',  attrs={'class': 'headline'})
title = ttl.text

#gets posted/edited time of the article
tme = soup.find('div', attrs={'class': 'storyPageMetaData-m__publish-time__19bdV storyPageMetaData-m__no-update__3AA06'})
time = tme.text

#gets author of the article
athr = soup.find('span', attrs={'class': 'contributor-name contributor-m__contributor-name__1-593 contributor-m__en-contributor-name__1DI3K'})
author = athr.text

#gets body of the article
bdy = soup.find('div', attrs={'class': 'story-element story-element-text'})
body = bdy.text

#array for the data collected
records = []
records.append((title, time, author, body))
print('Article Crawl Successful.')

#writes data to the csv file
import pandas as pd
df = pd.DataFrame(records, columns=['title', 'time', 'author', 'body'])
df.to_csv('ProthomAlo_ArticleDetails.csv', index=False, encoding='utf-8')

#confirmation
print('Data Write Successful')