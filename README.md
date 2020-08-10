# HackerNews

# Purpose
As a programmer, you walways want to stay up to date with the latest news in the tech industry. Technology is always changing and improving our way of living. As a user I want to create a bot that will sort the articles based on the amount of points the article has. 

# Requirements
 * Latest Version of Python
 * Import Request- allow us to download the index html from Hacker News
 * Import Beautiful Soup - Allows ud to gt the information from Hacker News website.
 *Import pprint- allow us to get an organized subtext.
 
 # Output
```````` 
 $ python scrape.py 
[{'link': 'https://www.federalreserve.gov/newsevents/pressreleases/other20200806a.htm',
  'title': 'Fed announces details of new interbank service to support instant '
           'payments',
  'votes': 606},
 {'link': 'https://capitalandgrowth.org/answers/Article/3323627/Microsoft-President-Brad-Smith-Why-We-Urgently-Need-a-Hippocratic-Oath-for-Software-Engineers?src=hn',
  'title': 'Microsoft President: We Need a Hippocratic Oath for Software '
           'Engineers',
  'votes': 447},
 {'link': 'https://woodgears.ca/heating/freezer.html',
  'title': 'How long does a freezer stay frozen when the power goes out?',
  'votes': 398},
 {'link': 'https://docs.house.gov/meetings/JU/JU05/20190716/109793/HHRG-116-JU05-20190716-SD015.pdf',
  'title': 'Statement on Google’s conduct by founder of CelebrityNetWorth.com '
           '(2019) [pdf]',
  'votes': 290},
 {'link': 'https://freedom-to-tinker.com/2013/10/09/the-linux-backdoor-attempt-of-2003/',
  'title': 'The Linux Backdoor Attempt of 2003 (2013)',
  'votes': 232},
 {'link': 'https://www.nytimes.com/2020/08/10/opinion/uber-ceo-dara-khosrowshahi-gig-workers-deserve-better.html',
  'title': 'I Am the CEO of Uber. Gig Workers Deserve Better',
  'votes': 226},
 {'link': 'https://superr.in/economy/i-tried-starting-a-manufacturing-unit-in-india/',
  'title': 'I tried starting a manufacturing unit in India',
  'votes': 179},
 {'link': 'https://www.gnu.org/philosophy/shouldbefree.en.html',
  'title': 'Why Software Should Be Free (2002)',
  'votes': 155},
 {'link': 'https://thephd.github.io/your-c-compiler-and-standard-library-will-not-help-you',
  'title': 'C will never stop you from making mistakes',
  'votes': 150},
 {'link': 'https://github.com/github/archive-program/blob/master/TheTechTree.md',
  'title': 'GitHub Arctic Code Vault: Tech Tree',
  'votes': 146},
 {'link': 'https://github.com/buraksezer/olric/releases/tag/v0.3.0-beta.1#=',
  'title': 'Distributed in-memory data structures in Go. Embeddable or '
           'independent service',
  'votes': 124},
 {'link': 'https://www.wired.com/story/nsa-tips-smartphone-data-canon-ransomware-twitter-bug-security-news/',
  'title': "NSA's Tips to Keep Your Phone from Tracking You",
  'votes': 101}]
  `````````
