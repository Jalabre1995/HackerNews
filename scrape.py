import requests #Allowa us to download the index html from Hacker News
from bs4 import BeautifulSoup #Allows us to get the information from Hacker News html page
from pprint import pprint
res = requests.get('https://news.ycombinator.com/news')
# Use BeautifulSoup to parse the text

soup = BeautifulSoup(res.text,'html.parser')
links = soup.select('.storylink')
subtext = soup.select('.subtext')

def create_custom_hn(links,votes):
    hn =[]
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace('points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})

    return hn
pprint = pprint
pprint(create_custom_hn(links,subtext))