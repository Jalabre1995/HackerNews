import requests #Allowa us to download the index html from Hacker News
from bs4 import BeautifulSoup #Allows us to get the information from Hacker News html page

res = requests.get('https://news.ycombinator.com/news')
# Use BeautifulSoup to parse the text

soup = BeautifulSoup(res.text,'html.parser')
links = soup.select('.storylink')
votes = soup.select('.score')

def create_custom_hn(links,votes):
    hn =[]
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href', None)
        points = int(votes[idx].getText().replace('points', ''))
        print(points)
        hn.append({'title': title, 'link': href})

    return hn
print(create_custom_hn(links,votes))