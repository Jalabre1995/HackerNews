import requests #Allowa us to download the index html from Hacker News
from bs4 import BeautifulSoup #Allows us to get the information from Hacker News html page

res = requests.get('https://news.ycombinator.com/news')
# Use BeautifulSoup to parse the text

soup = BeautifulSoup(res.text,'html.parser')
links = soup.select('.storylink')
votes = soup.select('.score')

print(votes[0])