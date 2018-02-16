
#! python3 
# lucky.py - Opens several Google search results. 

import requests, bs4

print('Finding release date...')
#res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
r = requests.get('http://funneldesigngroup.com/')
r.raise_for_status()
soup = bs4.BeautifulSoup(r.text, "lxml")


### Fix this later - not understanding why my string comes up empty
# releasedate = soup.find_all('div', attrs={'class':'mod'})[0].text
releasedate = soup.select('div.item.col-md-3')
releasedate